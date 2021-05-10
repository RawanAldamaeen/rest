from rest_framework import generics
from users.serializers import users_serializer
from django.contrib.auth.models import User


class UserDetails(generics.RetrieveAPIView):    # User detail view
    queryset = User.objects.all()
    serializer_class = users_serializer.UserSerializer
