from .models import Dog
from rest_framework import serializers


class DogModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dog
        fields = "__all__"