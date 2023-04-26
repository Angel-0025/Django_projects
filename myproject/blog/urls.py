from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("post/", views.newPost, name="new-post"),
    

    
    #path("post/<str:pk>", views.viewPost, name="view-post"),
]
