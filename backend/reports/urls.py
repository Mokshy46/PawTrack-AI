from django.urls import path
from .views import DogReportListAPIView, DogReportCreateAPIView

urlpatterns = [
    path('list/', DogReportListAPIView.as_view(), name='report'),
    path('create/', DogReportCreateAPIView.as_view(), name='create-report')
]
