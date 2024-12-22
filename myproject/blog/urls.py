from django.urls import path
from .views.auth_view import register,login
from .views.crud_view import create,edit,single_blog,home

urlpatterns = [
    path('register',register),
    path('login',login),
    path('',home),
    path('create/',create),
    path('edit',edit),
    path('single_blog',single_blog)
]
