from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/login', views.LoginAPIView.as_view()),
    path('users/new', views.UserCreate.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('users/<int:pk>/delete', views.UserDestroy.as_view()),
    path('users/<int:pk>/update', views.UserUpdate.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
