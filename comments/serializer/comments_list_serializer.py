from rest_framework import serializers
from comments.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):  # Comment GET request serializer
    class Meta:
        model = Comment
        fields = ["post_id", "name", "email", "text", "created_on"]
