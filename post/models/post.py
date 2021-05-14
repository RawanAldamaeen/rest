from django.conf import settings
from django.db import models


class Post(models.Model):
    id = models.AutoField(verbose_name='ID', primary_key=True)
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200, default='')
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content_ar = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    post_rate = models.IntegerField(default='0')
    total_rate = models.IntegerField(default='5')

    def __str__(self):
        return self.title