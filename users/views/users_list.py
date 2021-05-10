from rest_framework import generics
# from serializers.users_serializer import UserSerializer
from users.serializers import users_serializer
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):  # All users list view
    queryset = User.objects.all()
    serializer_class = users_serializer.UserSerializer