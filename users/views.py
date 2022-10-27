from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from users.serializer import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,    
)

# Create your views here.

class UserVeiw(APIView):
    def post(seif, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료"},status=status.HTTP_201_CREATED )
        else :
            return Response({"message":"f{serializer.errors}"},status=status.HTTP_400_BAD_REQUEST )



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class MockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(seif, request):
        return Response('get요청')