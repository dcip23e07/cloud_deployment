from django.urls import path

from todo.views import (
    ToDoListView,
    ToDoDetailView,
    GenericTodoDetailView,
    GenericTodoListView
)


app_name = 'Todo'
urlpatterns = [
    path('todo/', GenericTodoListView.as_view(), name='todos'),
    path('todo/<int:pk>/', GenericTodoDetailView.as_view(), name='single_todo_item'),
]