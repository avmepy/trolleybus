from django.contrib import admin
from django.urls import path, include

from main.views import TrolleybusView

urlpatterns = [
    path('trolleybus/<int:trolleybus_id>/', TrolleybusView.as_view())
]