from django.urls import path

from .views import (
    register_user,
    user_list,
    user_detail,
    create_group,
    join_group,
    my_group
)
from django.urls import path, include

urlpatterns = [
    
    path(
        'groups/create/',
        create_group,
        name='create-group'
    ),
    # Public
    path(
        'register/',
        register_user,
        name='register-user'
    ),

    # Protected
    path(
        'users/',
        user_list,
        name='user-list'
    ),

    path(
        'users/<int:pk>/',
        user_detail,
        name='user-detail'
    ),
    path(
        'groups/join/',
        join_group,
        name='join-group'
    ),
    path(
        'groups/my-group/',
        my_group,
        name='my-group'
    ),
    path('assignments/', include('assignments.urls')),
    path('tasks/', include('tasks.urls')),
]
