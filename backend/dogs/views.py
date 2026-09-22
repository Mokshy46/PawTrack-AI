from .serializers import DogModelSerializer
from .models import Dog
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView

User = get_user_model()



class DogReportCreateAPIView(CreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogModelSerializer
    # permission_classes = [IsAuthenticated]





