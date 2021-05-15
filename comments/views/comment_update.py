from rest_framework import authentication, status
from rest_framework.response import Response
from rest_framework.views import APIView
from comments.models.comment import Comment
from comments.serializer import comments_update_serializer


class CommentUpdate(APIView):  # Update comment data view
    queryset = Comment.objects.all()
    serializer_class = comments_update_serializer.UserUpdateCommentsSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    lookup_field = 'pk'

    def patch(self, request, *args, **kwargs):    # Perform PATCH request
        data = request.data
        pk = self.kwargs.get('pk')
        comment = Comment.objects.get(pk=pk)
        print(request.user.username)
        print(comment.name)
        if comment.name != request.user.username:
            return Response(status=status.HTTP_403_FORBIDDEN, data={"status": status.HTTP_403_FORBIDDEN, 'message': ('your not allowed to modify this comment'), 'meta': {}})

        comment.text = data.get('text', comment.text)
        comment.save()

        serializer = comments_update_serializer.UserUpdateCommentsSerializer(comment)
        return Response(status=status.HTTP_200_OK, data={"status": status.HTTP_200_OK, "data": serializer.data, 'meta': {}})
