from rest_framework import generics, permissions, authentication
from users.serializers import update_user_serializer
from django.contrib.auth.models import User


class UserUpdate(generics.UpdateAPIView):   # Update user data view
    queryset = User.objects.all()
    serializer_class = update_user_serializer.UpdateUserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    lookup_field = 'pk'