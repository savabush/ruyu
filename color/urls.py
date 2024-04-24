from django.urls import path, include
from rest_framework import routers

from color.viewsets import ColorViewSet, PaletteViewSet

color_router = routers.DefaultRouter()
color_router.register(r'', ColorViewSet)

palette_router = routers.DefaultRouter()
palette_router.register(r'', PaletteViewSet)

urlpatterns = [
    path('color/', include(color_router.urls)),
    path('palette/', include(palette_router.urls)),
]
