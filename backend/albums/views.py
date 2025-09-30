from .models import Album
from django.contrib.auth.models import User
from .serializers import UserSerializer, AlbumSerializer
from rest_framework import generics, viewsets, permissions

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Album.objects.filter(owner = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)