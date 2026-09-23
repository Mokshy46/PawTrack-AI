from .serializers import ActivityEventModelSerialzer
from .models import ActivityEvent
from rest_framework.generics import CreateAPIView



class ActivityEventCreateAPIView(CreateAPIView):
    queryset = ActivityEvent.objects.all()
    serializer_class = ActivityEventModelSerialzer



