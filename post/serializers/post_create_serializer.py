from rest_framework import serializers
from post.models.post import Post


class CreatePostSerializer(serializers.ModelSerializer):  # Post create request serializer
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=500)
    title_ar = serializers.CharField(max_length=100)
    content_ar = serializers.CharField(max_length=500)

    class Meta:
        model = Post
        fields = ["title", "content", "title_ar", "content_ar"]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
