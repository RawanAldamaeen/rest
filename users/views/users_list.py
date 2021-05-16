
from rest_framework import generics, status, pagination
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from users.serializers import users_serializer
from django.contrib.auth.models import User


class UsersPagination(pagination.PageNumberPagination):     # user list pagination settings
    default_limit = 2
    max_limit = 20

    def get_paginated_response(self, data):     # function to return the list of users with pagination data
        search = self.request.query_params.get('search')
        if search is None:
            search = ''
        return Response({
            "status": status.HTTP_200_OK,
            'data': data,
            'meta': {
                'count': self.page.paginator.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'search': search,
            }
        })


class UserList(generics.ListAPIView):  # All users list view
    queryset = User.objects.all()
    serializer_class = users_serializer.UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ('id', 'username', 'email',)
    pagination_class = UsersPagination

    def list(self, request, *args, **kwargs):
        users = User.objects.all()
        page = self.paginate_queryset(users)
        serializer = users_serializer.UserSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

