from django.urls import path
from .views import units, assignments, group_assignments, submissions

urlpatterns = [
    path('units/', units),
    path('assignments/', assignments),
    path('group-assignments/', group_assignments),
    path('submissions/', submissions),
]