from .models import Album
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password']
        )
        return user

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'artist', 'rating', 'review', 'created_at')