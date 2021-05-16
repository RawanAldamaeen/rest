from rest_framework import authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView
from post.models.post import Post
from post.serializers import post_update_serializer


class PostUpdate(APIView):  # Update post data view
    queryset = Post.objects.all()
    serializer_class = post_update_serializer.UpdatePostSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):    # Perform PUT request
        data = request.data
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        if not post.author_id == request.user:
            return Response(status=status.HTTP_403_FORBIDDEN, data={"status": status.HTTP_403_FORBIDDEN, 'message': ('your not allowed to modify this post'), 'meta': {}})

        post.title = data['title']
        post.content = data['content']
        post.title_ar = data['title_ar']
        post.content_ar = data['content_ar']
        post.save()

        serializer = post_update_serializer.UpdatePostSerializer(post)
        return Response(status=status.HTTP_200_OK, data={"status": status.HTTP_200_OK, "data": serializer.data, 'meta': {}})

    def patch(self, request, *args, **kwargs):    # Perform PATCH request
        data = request.data
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)

        if post.author_id != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN, data={"status": status.HTTP_403_FORBIDDEN, 'message': ('your not allowed to modify this post'), 'meta': {}})

        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        post.title_ar = data.get('title_ar', post.title_ar)
        post.content_ar = data.get('content_ar', post.content_ar)
        post.save()

        serializer = post_update_serializer.UpdatePostSerializer(post)
        return Response(status=status.HTTP_200_OK, data={"status": status.HTTP_200_OK, "data": serializer.data, 'meta': {}})
