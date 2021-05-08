from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
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
    serializer_class = serializers.UpdateUserSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDestroy(generics.DestroyAPIView):     # Delete user view
    queryset = User.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        user_username = request.data.get('pk')
        response = super().delete(request, *args, **kwargs)
        return response
