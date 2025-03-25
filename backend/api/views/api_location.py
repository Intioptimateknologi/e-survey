from django.http import HttpResponse
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

from api.serializers import location_serializer as serializers
from location import models
from api.views.filters import filter_location as custom_filters
from core.pagination import ItemPagination

class DesaViewSet(viewsets.ModelViewSet):
    queryset = models.desa.objects.all()
    serializer_class = serializers.DesaSerializer
    filter_backends = [DjangoFilterBackend, ]
    permission_classes = [permissions.AllowAny]
    filterset_class = custom_filters.DesaFilter

class KecamatanViewSet(viewsets.ModelViewSet):
    queryset = models.kecamatan.objects.all()
    serializer_class = serializers.KecamatanSerializer
    filter_backends = [DjangoFilterBackend, ]
    permission_classes = [permissions.AllowAny]
    filterset_class = custom_filters.KecamatanFilter

class KabupatenViewSet(viewsets.ModelViewSet):
    queryset = models.kabupaten.objects.all()
    serializer_class = serializers.KabupatenSerializer
    filter_backends = [DjangoFilterBackend, ]
    permission_classes = [permissions.AllowAny]
    filterset_class = custom_filters.KabupatenFilter

class ProvinsiViewSet(viewsets.ModelViewSet):
    queryset = models.provinsi.objects.all()
    serializer_class = serializers.ProvinsiSerializer
    filter_backends = [DjangoFilterBackend, ]
    permission_classes = [permissions.AllowAny]