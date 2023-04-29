from django.urls import path
from . import views


urlpatterns = [
 
    path("todolist/", views.toDoList, name="todolist-view"),
    path("todolist-create/", views.toDoList_create, name="todolist-create"),
]