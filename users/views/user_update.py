from rest_framework import generics, authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import update_user_serializer
from django.contrib.auth.models import User


class UserUpdate(APIView):  # Update user data view
    queryset = User.objects.all()
    serializer_class = update_user_serializer.UpdateUserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    lookup_field = 'pk'

    def get_queryset(self):
        user = User.objects.all()
        return user

    def put(self, request, *args, **kwargs):    # Perform Put request
        print('test')
        # user_object = self.get_object()
        data = request.data
        print(data)
        user = User.objects.get(username=data["username"])

        user.username = data['username']
        user.password = data['password']
        user.email = data['email']

        user.save()

        serializer = update_user_serializer.UpdateUserSerializer(user)

        return Response({"status": status.HTTP_200_OK, "data": serializer.data})

    def patch(self, request, *args, **kwargs):    # Perform Put request
        data = request.data
        print('test')
        pk = self.kwargs.get('pk')
        print(pk)
        print(data)
        user = User.objects.get(pk=pk)

        user.username = data.get('username', user.username)
        user.password = data.get('password', user.password)
        user.email = data.get('email', user.email)

        user.save()

        serializer = update_user_serializer.UpdateUserSerializer(user)

        return Response({"status": status.HTTP_200_OK, "data": serializer.data})
