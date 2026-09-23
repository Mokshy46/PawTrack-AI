from django.urls import path
from .views import UserCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name= "login"),
    path('token/refresh/', TokenRefreshView.as_view(), name= "refresh"),
]
