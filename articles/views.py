from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from articles import serializers
from articles.serializers import ArticleSerializer, ArticleListSerializer, ArticleCreateSerializer, CommentSerializer, CommentCreateSerializer
from users.serializer import UserProfileSerializer

from articles.models import Article , Comment
from users.models import User

# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleListSerializer(article, many=True) #윗줄을 보면 all() 전부다 가지고 왔기 때문에 즉 쿼리셋을 가지고 왔을때에는 many=True를 써준다 하나만 가지고 오게 되면 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleCreateSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ArticleDetailView(APIView):
    def get(self, request, article_id):
       
        article = get_object_or_404(Article, id=article_id) #모델 입력해주고 인자값을 입력해준다       
        serializer = ArticleSerializer(article) #윗줄28번째을 보면 all() 전부다 가지고 오는게 아니고 get 특정것 하나만 가지고 오기때문에 때문에 many=True를 안써준다
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request,article_id):
        article = Article.objects.get(id=article_id)
        if request.user == article.user:
            serializer = ArticleCreateSerializer(article, data=request.data) 
            if serializer.is_valid():
                serializer.save
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else :
            return Response('권한이 없습니다',status=status.HTTP_403_FORBIDDEN )
        

    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('권한이 없습니다', status=status.HTTP_400_BAD_REQUEST)
            


class CommentView(APIView):
    def get(self, request ,article_id):
        article = Article.objects.get(id=article_id)
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  

    def post(self, request ,article_id):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, article_id=article_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        pass

class CommentDetailView(APIView):
    def put(self, request ,article_id, comment_id):
        comment = Article.objects.get(id=article_id)
        if request.user == comment.user:
            serializer = CommentCreateSerializer(comment, data=request.data) 
            if serializer.is_valid():
                serializer.save
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else :
            return Response('권한이 없습니다',status=status.HTTP_403_FORBIDDEN )

    def delete(self, request ,article_id, comment_id):
        comment = get_object_or_404(Comment, id=article_id)
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('권한이 없습니다', status=status.HTTP_400_BAD_REQUEST)

class LikeView(APIView):
    def post(self, request ,article_id, comment_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.likes.remove(request.user):
            return Response("좋아요했습니다", status=status.HTTP_204_NO_CONTENT)
        else:
            article.likes.add(request.user)
            return Response('좋아요취소했습니다', status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer
        return Response('get 요청')
