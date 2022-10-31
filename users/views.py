from email import message
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from users.models import User
from users.serializer import CustomTokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,    
)
from rest_framework.generics import get_object_or_404
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

class FollowView(APIView):
    def post(self, request ,user_id, comment_id):
        you = get_object_or_404(User, id=user_id)
        me =request.user
        if me in you.follower.all():
            you.followers.remove(me)
            return Response("unfollow했습니다", status=status.HTTP_204_NO_CONTENT)
        else:
            you.follower.add(me)
            return Response('follow했습니다', status=status.HTTP_400_BAD_REQUEST)
