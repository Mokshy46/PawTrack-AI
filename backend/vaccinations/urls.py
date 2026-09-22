from django.urls import path
from .views import VaccinationRecordCreateAPIView

urlpatterns = [
    path('record/', VaccinationRecordCreateAPIView.as_view(), name='record')
]
