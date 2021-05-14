
from rest_framework import generics, status, pagination
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from post.serializers import post_list_serializer
from post.models.post import Post


class PostPagination(pagination.PageNumberPagination):     # post list pagination settings
    default_limit = 2
    max_limit = 20

    def get_paginated_response(self, data):     # function to return the list of posts with pagination data
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


class PostList(generics.ListAPIView):  # All posts list view
    queryset = Post.objects.all()
    serializer_class = post_list_serializer.PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ("author_id", "title", "content", )
    pagination_class = PostPagination

    def list(self, request, *args, **kwargs):
        posts = Post.objects.all()
        page = self.paginate_queryset(posts)

        lan = self.request.query_params.get('Language_code')
        if lan == 'ar':
            serializer = post_list_serializer.PostArSerializer(page, many=True)
        else:
            serializer = post_list_serializer.PostSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

