#!/usr/bin/env python3
# -*-encoding: utf-8-*-

from django.urls import path
from accounts.views import RegistrationAPIView


app_name = 'authentication'

urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
]
