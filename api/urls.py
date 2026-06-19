from django.urls import path

from .views import (
    register_user,
    user_list,
    user_detail
)

urlpatterns = [

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
]
