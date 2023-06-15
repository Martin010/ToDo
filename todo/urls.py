from django.urls import path, include

from todo import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
]