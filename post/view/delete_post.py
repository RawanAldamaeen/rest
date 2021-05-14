from rest_framework import generics, status
from rest_framework.response import Response
from post.models.post import Post


class PostDestroy(generics.DestroyAPIView):     # Delete post view
    queryset = Post.objects.all()
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        if post.author_id != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN, data={"status": status.HTTP_403_FORBIDDEN, 'message': ('your not allowed to delete this post'), 'meta': {}})

        super().delete(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK, data={"status": status.HTTP_200_OK, 'meta': {}})
