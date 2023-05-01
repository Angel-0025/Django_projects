from django.urls import path
from . import views


urlpatterns = [
 
    path("todolist/", views.toDoList, name="todolist"),
    path("todolist-view/<int:pk>", views.toDoList_view, name="todolist-view"),
    path("todolist-create/", views.toDoList_create, name="todolist-create"),
    path("todolist-update/<int:pk>", views.toDoList_update, name="todolist-update"),
    path("todolist-delete/<int:pk>", views.toDoList_delete, name="todolist-delete"),
]