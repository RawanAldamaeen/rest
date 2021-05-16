
from rest_framework import generics, status, pagination
from rest_framework.response import Response
from comments.models.comment import Comment
from comments.serializer import comments_list_serializer


class CommentsPagination(pagination.PageNumberPagination):     # comments list pagination settings
    default_limit = 10
    max_limit = 20

    def get_paginated_response(self, data):     # function to return the list of comments with pagination data

        return Response({
            "status": status.HTTP_200_OK,
            'data': data,
            'meta': {
                'count': self.page.paginator.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            }
        })


class CommentsList(generics.ListAPIView):  # All comments list view
    queryset = Comment.objects.all()
    serializer_class = comments_list_serializer.CommentSerializer
    pagination_class = CommentsPagination

    def list(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        page = self.paginate_queryset(comments)

        serializer = comments_list_serializer.CommentSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)

