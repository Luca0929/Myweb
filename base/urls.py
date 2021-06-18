from django.contrib import admin
from django.urls import path
from .views import PostList, CreatePost, DeletePost, EditPost, PostDetail, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', PostList.as_view(), name='post_list'),
    path('post_create/', CreatePost.as_view(), name='post_create'),
    path('post_delete/<int:pk>', DeletePost.as_view(), name='post_delete'),
    path('post_edit/<int:pk>', EditPost.as_view(), name='post_edit'),
    path('post_detail/<int:pk>', PostDetail.as_view(), name='post_detail'),
]