#!/usr/bin/env python3
# -*-encoding: utf-8-*-


from django.urls import path
from accounts.views import LoginView, LogoutView, ProfileView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
