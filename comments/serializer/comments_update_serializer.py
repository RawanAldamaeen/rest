from rest_framework import serializers
from comments.models.comment import Comment


class UserUpdateCommentsSerializer(serializers.ModelSerializer):  # Comment update request serializer
    text = serializers.CharField(max_length=500)

    class Meta:
        model = Comment
        fields = ["text"]





