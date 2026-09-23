from rest_framework import serializers
from .models import ActivityEvent

class ActivityEventModelSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityEvent
        fields = '__all__'