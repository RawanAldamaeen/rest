from rest_framework import generics
from users.serializers import create_user_serializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class UserCreate(generics.CreateAPIView):   # create new user view
    queryset = User.objects.all()
    serializer_class = create_user_serializer.CreateUserSerializer

    def post(self, request, **kwargs):
        serializer = create_user_serializer.CreateUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": status.HTTP_422_UNPROCESSABLE_ENTITY, "data": serializer.errors, 'meta': {}})

        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data={"status": status.HTTP_201_CREATED, "data": serializer.data, 'meta': {}})
