from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import user_create as user_create
from .views import user_delete as user_delete
from .views import users_list as user_list
from .views import user_update as user_update
from .views import user_details as user_deteail


urlpatterns = [
    path('users/', user_list.UserList.as_view()),
    path('users/new', user_create.UserCreate.as_view()),
    path('users/<int:pk>/', user_deteail.UserDetails.as_view()),
    path('users/<int:pk>/delete', user_delete.UserDestroy.as_view()),
    path('users/<int:pk>/update', user_update.UserUpdate.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
