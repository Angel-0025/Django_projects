from django.urls import path
from . import views

urlpatterns = [
    path("todolist-view/", views.todolist_view, name="todolist-view"),
    path("todolist-create", views.todolist_create, name="todolist-create"),
    path("todolist-delete/<int:pk>", views.todolist_delete, name="todolist-delete"),
    
    path("dolist-view/<str:pk>", views.dolist_view, name="dolist-view"),
    path("dolist-create/<str:pk>", views.dolist_create, name="dolist-create"),
    path("dolist-update/<int:pk>", views.dolist_update, name="dolist-update"),
    
    path("dolist-delete/<int:pk>", views.dolist_delete, name="dolist-delete"),
    

]