from rest_framework import serializers
from post.models.post import Post


class PostSerializer(serializers.ModelSerializer):  # Post GET request serializer
    class Meta:
        model = Post
        fields = ["id", "author_id", "title", "content", "created_on"]


class PostArSerializer(serializers.ModelSerializer):  # Arabic post GET request serializer
    class Meta:
        model = Post
        fields = ["id", "author_id", "title_ar", "content_ar", "created_on"]





