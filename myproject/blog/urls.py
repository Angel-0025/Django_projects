from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.newPost, name="new-post"),
    
    path("post/view/<int:pk>", views.viewPost, name="view-post"),
    path("user/post-list/<int:pk>", views.userPostList, name="user-post-list"),
    
    path("post/edit/<int:pk>", views.editPost, name="edit-post"),
    path("post/delete/<int:pk>", views.deletePosted, name="delete-post"),
]
