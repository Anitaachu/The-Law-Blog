from django.contrib import admin
from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views 


urlpatterns = [
    path('', views.index, name="index"),
    path('index.html/', views.index, name="index"),
    path('blog.html/', PostListView.as_view(), name="blog"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('add_post.html/', views.add_post, name="add_post"),
    path('about.html/', views.about, name="about"),
] 