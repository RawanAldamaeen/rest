from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):  # User GET request serializer
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']




