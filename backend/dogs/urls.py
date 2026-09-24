from django.urls import path
from .views import DogCreateAPIView,DogListAPIView


urlpatterns = [
    path('create/', DogCreateAPIView.as_view(), name='create'),
    path('list/', DogListAPIView.as_view(), name='list'),
]

