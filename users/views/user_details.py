from rest_framework import generics, status
from users.serializers import users_serializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class UserDetails(generics.RetrieveAPIView):    # User detail view
    queryset = User.objects.all()
    serializer_class = users_serializer.UserSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):    # function to return the response of user detail
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        serializer = users_serializer.UserSerializer(user)
        return Response(status=status.HTTP_200_OK, data={"status": status.HTTP_200_OK, "data": serializer.data, 'meta': {}})


