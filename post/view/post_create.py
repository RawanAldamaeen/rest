from rest_framework import generics, permissions,viewsets
from post.serializers import post_create_serializer
from rest_framework.response import Response
from rest_framework import status
from post.models.post import Post


class PostCreate(generics.CreateAPIView):   # create new post view
    queryset = Post.objects.all()
    serializer_class = post_create_serializer.CreatePostSerializer

    def post(self, request, *args, **kwargs):
        print(request.user)
        serializer = post_create_serializer.CreatePostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": status.HTTP_422_UNPROCESSABLE_ENTITY, "data": serializer.errors, 'meta': {}})

        serializer.save(author_id=request.user)
        return Response({"status": status.HTTP_200_OK, "data": serializer.data, 'meta': {}})
