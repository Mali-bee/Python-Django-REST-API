from django.urls import path
from .views import get_users, create_user, user_detail

urlpatterns = [
    path('users/', get_users, name='get_users'),                          #the USERS url route
    path('users/create/', create_user, name='create_user'),               #the CREATE url route
    path('users/<int:pk>', user_detail, name='user_detail')               #route to a specific user via the user's primary key - pk
]