#!/usr/bin/env python3
# -*-encoding: utf-8-*-


from django.urls import path, include
from routes.views import HomeView


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
]
