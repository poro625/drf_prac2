from rest_framework import serializers
from articles.models import Article, Comment



class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "image","content")



class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = "__all__"

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content",)


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    Comment_set = CommentSerializer(many=True)
    likes = serializers.StringRelatedField(many=True)

    def get_user(self, obj): # obj는 Article의 DB의미 get_(0000)과 obj.0000.email 0000맞춰줘야한다
        return obj.user.email

    class Meta:
        model = Article
        exclude = ("article",)


class ArticleListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_user(self, obj): # obj는 Article의 DB의미 get_(0000)과 obj.0000.email 0000맞춰줘야한다
        return obj.user.email

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Article
        fields = ("pk", "title", "image", "updated_at", "user","likes_count", "comments",)