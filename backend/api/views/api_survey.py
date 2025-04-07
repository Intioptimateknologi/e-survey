import uuid
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core.exceptions import BadRequest
from rest_framework.exceptions import ValidationError
from django.contrib.auth import login
from django.utils import timezone
from django.db.models import Count, Exists, Max, OuterRef, Func, IntegerField, F
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.db.models import Q

from api.serializers import survey_serializer as serializers
from survey import models
from core.pagination import ItemPagination

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = models.survey.objects.all()
    serializer_class = serializers.SurveySerializer
    filter_backends = [DjangoFilterBackend, ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['created_by']

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return models.survey.objects.none()

        if user.profile.role == 'admin':
            return models.survey.objects.all()
        return models.survey.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, code=uuid.uuid4().hex)

    def get_object(self):
        """Allow lookup by both `id` and `code`"""
        queryset = self.get_queryset()
        lookup_value = self.kwargs.get("pk")  # Default lookup parameter

        if lookup_value.isdigit():  # If pk is numeric, assume it's an ID
            obj = get_object_or_404(queryset, id=int(lookup_value))
        else:  # Otherwise, assume it's a code
            obj = get_object_or_404(queryset, code=lookup_value)

        self.check_object_permissions(self.request, obj)
        return obj

class RespondentViewSet(viewsets.ModelViewSet):
    queryset = models.respondent.objects.all()
    serializer_class = serializers.RespondentSerializer
    filter_backends = [DjangoFilterBackend, ]
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['survey']

    def perform_create(self, serializer):
        survey_id = serializer.validated_data.get('survey')
        if isinstance(survey_id, models.survey):
            survey_instance = survey_id
        else:
            survey_instance = models.survey.objects.get(id=survey_id)
        current_respondents = models.respondent.objects.filter(survey=survey_instance).count()
        if current_respondents >= survey_instance.limit:
            raise ValidationError({"detail": "The number of respondents has already reached the maximum limit."})

        serializer.save()