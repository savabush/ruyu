from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, response
from rest_framework.permissions import IsAuthenticated

from color.filters import ColorFilter
from color.models import Color, Palette
from color.permissions import IsOwnerProfileOrReadOnly
from color.serializers import GetColorSerializer, CreateColorSerializer, GetPaletteSerializer, CreatePaletteSerializer

from drf_spectacular.utils import extend_schema


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)
    http_method_names = ('get', 'post', 'patch', 'delete')
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ColorFilter

    def get_queryset(self):
        user = self.request.user
        return Color.objects.filter(palette__user=user).order_by('name')

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return GetColorSerializer
        return CreateColorSerializer

    @extend_schema(responses=GetColorSerializer)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = GetColorSerializer(serializer.instance)
        return response.Response(serializer.data, headers=headers)

    @extend_schema(responses=GetPaletteSerializer)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        serializer = GetColorSerializer(serializer.instance)

        return response.Response(serializer.data)


class PaletteViewSet(viewsets.ModelViewSet):
    queryset = Palette.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)
    http_method_names = ('get', 'post', 'patch', 'delete')

    def get_queryset(self):
        user = self.request.user
        return Palette.objects.filter(user=user).order_by('name')

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return GetPaletteSerializer
        return CreatePaletteSerializer

    @extend_schema(responses=GetPaletteSerializer)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = GetPaletteSerializer(serializer.instance)
        return response.Response(serializer.data, headers=headers)

    @extend_schema(responses=GetPaletteSerializer)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        serializer = GetPaletteSerializer(serializer.instance)

        return response.Response(serializer.data)
