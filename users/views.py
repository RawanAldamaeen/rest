from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):  # All users list view
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetails(generics.RetrieveAPIView):    # User detail view
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreate(generics.CreateAPIView):   # create new user view
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserUpdate(generics.UpdateAPIView):   # Update user data view
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserDestroy(generics.DestroyAPIView):     # Delete user view
    queryset = User.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        user_username = request.data.get('pk')
        response = super().delete(request, *args, **kwargs)
        return response
