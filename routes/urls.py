#!/usr/bin/env python3
# -*-encoding: utf-8-*-


from django.urls import path
from routes.views import HomeView, ScheduleView, ReportView


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('schedules/', ScheduleView.as_view(), name='schedules'),
    path('reports/', ReportView.as_view(), name='reports'),
]
