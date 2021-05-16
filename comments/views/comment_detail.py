from rest_framework import generics, status
from rest_framework.response import Response
from comments.models.comment import Comment
from comments.serializer import comments_list_serializer


class CommentDetails(generics.RetrieveAPIView):    # comment detail view
    queryset = Comment.objects.all()
    serializer_class = comments_list_serializer.CommentSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):    # function to return the response of comment detail
        pk = self.kwargs.get('pk')
        comment = Comment.objects.get(pk=pk)
        serializer = comments_list_serializer.CommentSerializer(comment)

        return Response({"status": status.HTTP_200_OK, "data": serializer.data, 'meta': {}})