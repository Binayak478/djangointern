from django.urls import path
from .views.auth_view import register,login

urlpatterns = [
    path('/register',register),
    path('/login',login)
]
