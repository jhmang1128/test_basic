from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        fields = ("id", "title", "content", "author", "created_at", "updated_at")


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "content")
