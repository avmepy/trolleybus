from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view()),  # url to get the token
    path('api/token/refresh/', TokenRefreshView.as_view()),  # url to refresh the token
]
