from rest_framework import generics, status
from rest_framework.response import Response
from comments.models.comment import Comment


class CommentDestroy(generics.DestroyAPIView):     # Delete comment view
    queryset = Comment.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        comment = Comment.objects.get(pk=pk)
        if comment.name != request.user.username:
            return Response(status=status.HTTP_403_FORBIDDEN, data={"status": status.HTTP_403_FORBIDDEN, 'message': ('your not allowed to delete this Comment'), 'meta': {}})

        super().delete(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK, data={"status": status.HTTP_200_OK, 'meta': {}})
