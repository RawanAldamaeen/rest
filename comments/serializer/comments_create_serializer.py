from rest_framework import serializers
from comments.models.comment import Comment


class UserCreateCommentsSerializer(serializers.ModelSerializer):  # User create Comment request serializer
    text = serializers.CharField(max_length=500)

    class Meta:
        model = Comment
        fields = ["post_id", "text"]

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)


class AnonymousUserCreateCommentsSerializer(serializers.ModelSerializer):  # Anonymous user create comment request serializer
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=250)
    text = serializers.CharField(max_length=500)

    class Meta:
        model = Comment
        fields = ["post_id", "name", "email", "text"]

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)