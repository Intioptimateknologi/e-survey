from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import ObjectDoesNotExist

from survey import models

class SurveySerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    code = serializers.ReadOnlyField()
    progress = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = models.survey
        exclude = []

    def get_status(self, obj):
        return {
            'time': obj.is_active,
            'enough': obj.is_enough
        }

    def get_progress(self, obj):
        try:
            filled = models.respondent.objects.filter(survey=obj).count()
            return filled
            return f'{filled}/{obj.limit}'
        except ObjectDoesNotExist:
            return 0

class RespondentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.respondent
        exclude = []

    def __init__(self, *args, **kwargs):
        super(RespondentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request:
            if request.method == 'GET':
                self.Meta.depth = 1
            elif request.method in ['DELETE', 'PUT', 'PATCH']:
                self.Meta.depth = 0