from rest_framework import generics, permissions, authentication
from rest_framework.authtoken.models import Token

from users.serializers import user_login_serializer
from django.contrib.auth.models import User, update_last_login
from rest_framework.response import Response
from rest_framework import status

class LoginAPIView(generics.GenericAPIView):    # User login view

    def post(self, request, *args, **kwargs):
        serializer = user_login_serializer.LoginSerializers(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key})