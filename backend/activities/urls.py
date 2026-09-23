from django.urls import path
from .views import ActivityEventCreateAPIView

urlpatterns = [
    path('', ActivityEventCreateAPIView.as_view(), name='activity')
]
