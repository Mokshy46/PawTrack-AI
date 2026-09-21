from django.urls import path
from .views import DogReportCreateAPIView


urlpatterns = [
    path('create/', DogReportCreateAPIView.as_view(), name='create')
]

