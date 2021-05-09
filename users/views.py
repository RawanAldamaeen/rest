from rest_framework import generics, permissions, authentication
from rest_framework.authtoken.models import Token

from . import serializers
from django.contrib.auth.models import User, update_last_login
from rest_framework.response import Response
from rest_framework import status


class UserList(generics.ListAPIView):  # All users list view
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetails(generics.RetrieveAPIView):    # User detail view
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreate(generics.CreateAPIView):   # create new user view
    serializer_class = serializers.CreateUserSerializer

    def post(self, request, **kwargs):
        serializer = serializers.CreateUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserUpdate(generics.UpdateAPIView):   # Update user data view
    queryset = User.objects.all()
    serializer_class = serializers.UpdateUserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    lookup_field = 'pk'

    #
    # def update(self, request, *args, **kwargs):
    #     serializer = serializers.UpdateUserSerializer(data=request.data, partial=True)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class UserDestroy(generics.DestroyAPIView):     # Delete user view
    queryset = User.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        user_username = request.data.get('pk')
        response = super().delete(request, *args, **kwargs)
        return response


class LoginAPIView(generics.GenericAPIView):    # User login view

    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginSerializers(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key})