from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import ObjectDoesNotExist

from api import models

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = models.profile
        exclude = []

    def get_user(self, obj):
        return UserOnlySerializer(obj.user).data

class UserOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        ]

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'profile',
            'email',
            'first_name',
            'last_name',
        ]

    def get_profile(self, obj):
        try:
            return ProfileSerializer(obj.profile).data
        except ObjectDoesNotExist:
            return None

class RegisterSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # profile = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        # models.profile.objects.create(
        #     user=user,
        #     **profile
        # )
        return user
