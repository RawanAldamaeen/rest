from rest_framework import generics
from django.contrib.auth.models import User


class UserDestroy(generics.DestroyAPIView):     # Delete user view
    queryset = User.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        user_username = request.data.get('pk')
        response = super().delete(request, *args, **kwargs)
        return response