#!/usr/bin/env python3
# -*-encoding: utf-8-*-


from django.urls import path
from routes.views import HomeView, ScheduleView


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('schedules/', ScheduleView.as_view(), name='schedules')
]
