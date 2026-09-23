from django.urls import path
from .views import DogCreateAPIView


urlpatterns = [
    path('create/', DogCreateAPIView.as_view(), name='create')
]

