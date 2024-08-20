# users/serializers.py
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  
        extra_kwargs = {'password': {'write_only': True}}

    # Override create method to hash passwords
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    # Generate Token For user
    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
