# djangoproject/urls.py
from django.contrib import admin
from django.urls import path
from tasks import views as task_views
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls), # Admin-Panel
    path('tasks/', task_views.home, name='tasks_home'),  # Hauptseite der tasks-App
    path('todo/', todo_views.home, name='todo_home'), #Hauptseite der Todo-App
    path('', task_views.home, name='home')
]
