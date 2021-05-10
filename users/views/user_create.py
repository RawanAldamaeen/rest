from rest_framework import generics
from users.serializers import create_user_serializer
from rest_framework.response import Response
from rest_framework import status


class UserCreate(generics.CreateAPIView):   # create new user view
    serializer_class = create_user_serializer.CreateUserSerializer

    def post(self, request, **kwargs):
        serializer = create_user_serializer.CreateUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)