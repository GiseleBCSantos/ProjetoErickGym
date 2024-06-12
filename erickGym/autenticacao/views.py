from django.shortcuts import render
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

# Create your views here.

class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    
class MeAPIView(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)