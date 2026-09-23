from .serializers import DogModelSerializer
from .models import Dog
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework import pagination

User = get_user_model()


class DogCreateAPIView(CreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogModelSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = pagination.PageNumberPagination








