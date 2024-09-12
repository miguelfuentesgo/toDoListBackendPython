
from django.contrib import admin
from django.urls import path, include
from .views import CreateTask, GetTask, DeleteTask, GetAll, UpdateTask

urlpatterns = [
    path('createTask', CreateTask, name="CreateTask"),
    path('getTask/<str:id>', GetTask, name="GetTask"),
    path('updateTask/<str:id>', UpdateTask, name="UpdateTask"),
    path('deleteTask/<str:id>', DeleteTask, name="DeleteTask"),
    path('getAll', GetAll, name="GetAllTasks")
]
