from rest_framework import generics, status
from rest_framework.response import Response
from post.serializers import post_list_serializer
from post.models.post import Post
from comments.models.comment import Comment
from comments.serializer import comments_list_serializer


class PostDetails(generics.RetrieveAPIView):    # post detail view
    queryset = Post.objects.all()
    serializer_class = post_list_serializer.PostSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):    # function to return the response of post detail
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        # post comments
        comment = Comment.objects.all().filter(post_id=post)
        comments_serializer = comments_list_serializer.CommentSerializer(comment, many=True)
        # post language
        lan = self.request.query_params.get('Language_code')
        if lan == 'ar':
            serializer = post_list_serializer.PostArSerializer(post)
        else:
            serializer = post_list_serializer.PostSerializer(post)

        return Response({"status": status.HTTP_200_OK, "data": serializer.data, "comments": comments_serializer.data, 'meta': {}})