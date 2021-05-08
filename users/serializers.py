from django.contrib.auth.password_validation import validate_password
from django.core import validators
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):  # User GET request serializer
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CreateUserSerializer(serializers.ModelSerializer):  # User Post request serializer
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(validators=[validate_password],
                                     style={'input_type': 'password', 'placeholder': 'Password'},
                                     max_length=30, write_only=True)
    email = serializers.EmailField(max_length=250, validators=[validators.validate_email])

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def validate(self, attrs):
        password = attrs.get('password', '')
        email = attrs.get('email', '')

        if len(password) < 8 or len(password) > 30:
            raise serializers.ValidationError(
                {'password': ('Password length should be between 8 - 30 characters')}
            )

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')}
            )

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UpdateUserSerializer(serializers.ModelSerializer):  # User PUT request serializer
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(validators=[validate_password],
                                     style={'input_type': 'password', 'placeholder': 'Password'},
                                     max_length=30, write_only=True)
    email = serializers.EmailField(max_length=250, validators=[validators.validate_email])

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def validate(self, attrs):
        password = attrs.get('password', '')
        if len(password) < 8 or len(password) > 30:
            raise serializers.ValidationError(
                {'password': ('Password length should be between 8 - 30 characters')}
            )

        return super().validate(attrs)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance