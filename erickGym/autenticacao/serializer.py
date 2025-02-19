from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
    
    
class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username'