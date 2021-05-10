from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.response import Response


class UserDestroy(generics.DestroyAPIView):     # Delete user view
    queryset = User.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        user_username = request.data.get('pk')
        response = super().delete(request, *args, **kwargs)
        return Response({"status": status.HTTP_200_OK, 'meta': {}})