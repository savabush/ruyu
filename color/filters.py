import django_filters

from color.models import Color


class ColorFilter(django_filters.FilterSet):
    class Meta:
        model = Color
        fields = ('palette',)