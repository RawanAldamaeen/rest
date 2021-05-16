from rest_framework import generics
from rest_framework.authtoken.models import Token

from users.serializers import user_login_serializer
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class LoginAPIView(generics.GenericAPIView):    # User login view
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = user_login_serializer.LoginSerializers(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response(status=status.HTTP_200_OK, data={"status": status.HTTP_200_OK, "Token": token.key, "meta": {}})