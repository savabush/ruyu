from rest_framework import viewsets, response, mixins
from django.db import transaction
from drf_spectacular.utils import extend_schema

from core.models import User
from core.serializers import GetUserSerializer, CreateUserSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return GetUserSerializer
        return CreateUserSerializer

    @transaction.atomic
    @extend_schema(responses=GetUserSerializer)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = GetUserSerializer(serializer.instance)
        return response.Response(serializer.data, headers=headers)
