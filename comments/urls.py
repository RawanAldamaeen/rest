from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import comments_list
from .views import comment_create
from .views import comment_detail
from .views import comment_update
from .views import comment_delete

urlpatterns = [
    path('comments/', comments_list.CommentsList.as_view()),
    path('comments/new', comment_create.CommentsCreate.as_view()),
    path('comments/<int:pk>/', comment_detail.CommentDetails.as_view()),
    path('comments/<int:pk>/update', comment_update.CommentUpdate.as_view()),
    path('comments/<int:pk>/delete', comment_delete.CommentDestroy.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)