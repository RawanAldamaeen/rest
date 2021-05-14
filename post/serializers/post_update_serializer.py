from rest_framework import serializers
from post.models.post import Post


class UpdatePostSerializer(serializers.ModelSerializer):  # Post update request serializer
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=500)
    title_ar = serializers.CharField(max_length=100)
    content_ar = serializers.CharField(max_length=500)

    class Meta:
        model = Post
        fields = ["title", "content", "title_ar", "content_ar"]