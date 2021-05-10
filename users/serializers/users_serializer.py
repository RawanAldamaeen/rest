from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):  # User GET request serializer
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']




