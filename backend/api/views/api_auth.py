from datetime import date, timedelta
from django.db.models.functions import TruncDate
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core.exceptions import BadRequest
from rest_framework.exceptions import ValidationError
from django.contrib.auth import login
from django.utils import timezone
from django.db.models import Count, Exists, Max, OuterRef, Func, IntegerField, F
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.db.models import Q

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.exceptions import InvalidToken

from api.serializers import auth_serializer as serializers
from core.pagination import ItemPagination
from api import models
from survey import models as survey_models
from location import models as location_models

class DashboardView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        admin_users = User.objects.filter(profile__role='admin').count()
        member_users = User.objects.filter(profile__role='member').count()
        users = admin_users + member_users
        surveys = survey_models.survey.objects.all().count()
        respondents = survey_models.respondent.objects.all().count()
        data = {
            'surveys': surveys,
            'respondents': respondents,
            'users': {
                'admin': admin_users,
                'member': member_users,
                'total': users
            },
        }

        # Charting
        # Ambil data 30 hari terakhir
        today = date.today()
        last_30_days = today - timedelta(days=30)

        # Trafik registrasi user member
        member_traffic = (
            User.objects.filter(profile__role='member', date_joined__gte=last_30_days)
            .annotate(date=TruncDate('date_joined'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('date')
        )

        # Trafik pengisian responden
        respondent_traffic = (
            survey_models.respondent.objects.filter(created_at__gte=last_30_days)
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('date')
        )

        # Trafik pembuatan survey
        survey_traffic = (
            survey_models.survey.objects.filter(created_at__gte=last_30_days)
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('date')
        )

        chart_data = {
            'member_registration': list(member_traffic),
            'respondent_filling': list(respondent_traffic),
            'survey_creation': list(survey_traffic),
        }

        return Response({
            'success': True,
            'message': 'Dashboard API',
            'data': data,
            'chart': chart_data
        }, status=status.HTTP_200_OK)

class RegisterView(CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        visible_password = request.data['password']
        user = serializer.save()
        profile = models.profile.objects.create(user=user, visible_password=visible_password)
        return Response({
            'success': True,
            'message': 'User berhasil dibuat',
            'user': serializers.UserSerializer(user).data,
        }, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ItemPagination

    @action(detail=False, methods=["post"])
    def verify_token(self, request):
        """Cek validitas access token"""
        serializer = TokenVerifySerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            return Response({"valid": True}, status=status.HTTP_200_OK)
        except InvalidToken:
            return Response({"valid": False, "message": "Invalid token"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'], url_path='me', name='me')
    def me(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'], url_path='update-password', name='Update Password')
    def update_password(self, request, pk=None):
        current_password = self.request.data.get('current_password', None)
        new_password = self.request.data.get('new_password', None)

        if not current_password or not new_password:
            return Response({
                'success': False,
                'error': 'New password and current password must be filled in.',
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=pk)
            username = user.username

            if not user.check_password(current_password):
                return Response({
                    'success': False,
                    'error': 'Your current password is incorrect.'
                }, status=status.HTTP_400_BAD_REQUEST)

            if new_password == current_password:
                return Response({
                    'success': False,
                    'error': 'New password must be different from current password.'
                }, status=status.HTTP_400_BAD_REQUEST)

            user.profile.visible_password = new_password
            user.profile.save()

            user.set_password(new_password)
            user.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return Response({
                'success': True,
                'message': f'Password for user {username} has been updated.',
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                'success': False,
                'error': f'User not found.',
            }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['PUT'], url_path='profile', name='Update Profile')
    def update_profile(self, request, pk=None):
        first_name = self.request.data.get('first_name', None)
        email = self.request.data.get('email', None)
        nik = self.request.data.get('nik', None)
        satker = self.request.data.get('satker', None)

        print('-> Updating user profile', {
            'first_name': first_name,
            'email': email,
            'nik': nik,
            'satker': satker
        })

        # if not first_name or not email or not satker or not nik:
        #     return Response({
        #         'success': False,
        #         'error': 'Terdapat beberapa inputan yang kosong.',
        #     }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(pk=pk)
            user.first_name = first_name
            user.email = email
            user.save()

            if satker:
                user.profile.satker_id = satker

            user.profile.nik = nik
            # if nik:

            user.profile.save()

            return Response({
                'success': True,
                'message': f'User profile for user {user.username} has been updated.',
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({
                'success': False,
                'error': f'User not found',
            }, status=status.HTTP_404_NOT_FOUND)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = models.profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.AllowAny]

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        data["user"] = serializers.UserSerializer(user).data
        return data

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer