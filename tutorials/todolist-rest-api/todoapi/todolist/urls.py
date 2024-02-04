from django.urls import path

from . import views

urlpatterns = [
  path('todos/', views.TodoListView.as_view()),
  path('todos/<str:id>/', views.TodoListView.as_view()),
]
