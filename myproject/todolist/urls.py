from django.urls import path
from . import views

urlpatterns = [
    path("todolist-view/", views.todolist_view, name="todolist-view"),
    path("todolist-create", views.todolist_create, name="todolist-create"),
    
    path("dolist-view/<int:pk>", views.dolist_view, name="dolist-view"),
    path("dolist-create/<str:pk>", views.dolist_create, name="dolist-create"),
]