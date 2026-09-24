from django.urls import path
from .views import DogCreateAPIView,DogListAPIView,DogDestroyAPIView,DogUpdateAPIView


urlpatterns = [
    path('create/', DogCreateAPIView.as_view(), name='dog-create'),
    path('list/', DogListAPIView.as_view(), name='dog-list'),
    path('delete/<uuid:pk>/', DogDestroyAPIView.as_view(), name='dog-delete'),
    path('update/<uuid:pk>/', DogUpdateAPIView.as_view(), name='dog-update'),
]

