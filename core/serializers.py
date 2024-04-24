from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from core.models import User


class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'name')


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        validate_password(validated_data['password'], user)
        return user
