from django.urls import path
from .views import VaccinationRecordCreateAPIView,VaccinationRecordListAPIView

urlpatterns = [
    path('create/', VaccinationRecordCreateAPIView.as_view(), name='create-record'),
    path('list/', VaccinationRecordListAPIView.as_view(), name='list-records')
]
