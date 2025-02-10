from django.urls import path
from .views import (
    TaskListView, TaskAddView,
    TaskUpdateView, TaskDeleteView,
    TaskPauseView, TaskCompleteView,
    TaskContinueView, get_time_spent,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('add/', TaskAddView.as_view(), name='add_task'),
    path('edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
    path('complete_task/<int:pk>/', TaskCompleteView.as_view(), name='complete_task'),
    path('pause_task/<int:pk>/', TaskPauseView.as_view(), name='pause_task'),
    path('continue_task/<int:pk>/', TaskContinueView.as_view(), name='continue_task'),
    path('get-time-spent/', get_time_spent, name='get_time_spent'),
]
