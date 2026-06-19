from django.urls import path
from .views import tasks, task_detail

urlpatterns = [
    path('', tasks),
    path('<int:pk>/', task_detail),
]