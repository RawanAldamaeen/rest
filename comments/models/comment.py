from django.db import models
from post.models.post import Post


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75, blank=True)
    text = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.name)