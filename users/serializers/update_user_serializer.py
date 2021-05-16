from django.contrib.auth.password_validation import validate_password
from django.core import validators
from rest_framework import serializers
from django.contrib.auth.models import User


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

