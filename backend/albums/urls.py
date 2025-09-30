from .views import AlbumViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'albums', AlbumViewSet, basename='album')

urlpatterns = [
    path('', include(router.urls)),
]