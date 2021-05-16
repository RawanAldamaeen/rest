from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from comments.models.comment import Comment
from comments.serializer import comments_create_serializer
from post.models.post import Post


class CommentsCreate(generics.CreateAPIView):   # create new comment view
    queryset = Comment.objects.all()

    def post(self, request, *args, **kwargs):
        post_id = Post.objects.get(id=request.data["post_id"])
        # anonymous user comment
        if request.user.is_anonymous:
            serializer = comments_create_serializer.AnonymousUserCreateCommentsSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({"status": status.HTTP_422_UNPROCESSABLE_ENTITY, "data": serializer.errors, 'meta': {}})
            serializer.save(post_id=post_id)
            return Response({"status": status.HTTP_200_OK, "data": serializer.data, 'meta': {}})
        # authenticate user comment
        serializer = comments_create_serializer.UserCreateCommentsSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": status.HTTP_422_UNPROCESSABLE_ENTITY, "data": serializer.errors, 'meta': {}})
        serializer.save(name=request.user, post_id=post_id, email=request.user.email)
        return Response({"status": status.HTTP_200_OK, "data": serializer.data, 'meta': {}})
