from rest_framework import serializers

from color.models import Color, Palette
from core.models import User


class GetColorSerializer(serializers.ModelSerializer):
    palette = serializers.ReadOnlyField(source='palette.name')

    class Meta:
        model = Color
        fields = ('id', 'name', 'hex', 'palette')


class CreateColorSerializer(serializers.ModelSerializer):
    palette = serializers.PrimaryKeyRelatedField(queryset=Palette.objects.all())

    class Meta:
        model = Color
        fields = ('id', 'hex', 'palette')


class GetPaletteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Palette
        fields = ('id', 'name', 'user')


class CreatePaletteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Palette
        fields = ('id', 'name', 'user')
