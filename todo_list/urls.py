from django.urls import path
from todo_list import views

urlpatterns = [
    path('todos', views.todo_list),
    path('todos/<int:pk>', views.todo_detail),
]
