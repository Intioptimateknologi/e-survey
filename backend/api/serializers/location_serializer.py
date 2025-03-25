from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import ObjectDoesNotExist

from location import models

class DesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.desa
        exclude = []

class KecamatanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.kecamatan
        exclude = []

class KabupatenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.kabupaten
        exclude = []

class ProvinsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.provinsi
        exclude = []