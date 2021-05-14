from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .view import post_create as post_create
from .view import post_list as post_list
from .view import post_detail as post_detail
from .view import post_update as post_update
from .view import delete_post as post_delete
urlpatterns = [
    path('posts/', post_list.PostList.as_view()),
    path('posts/new', post_create.PostCreate.as_view()),
    path('posts/<int:pk>/', post_detail.PostDetails.as_view()),
    path('posts/<int:pk>/update', post_update.PostUpdate.as_view()),
    path('posts/<int:pk>/delete', post_delete.PostDestroy.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)