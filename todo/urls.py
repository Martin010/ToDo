from django.urls import path, include

from todo import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark-as-done/<int:pk>/', views.mark_as_done, name='mark-as-done'),
    path('mark-as-undone/<int:pk>/', views.mark_as_undone, name='mark-as-undone'),
    path('edit-task/<int:pk>/', views.edit_task, name='edit-task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete-task'),
]