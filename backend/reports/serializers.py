from rest_framework import serializers
from .models import DogReport


class DogReportModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DogReport
        fields = '__all__'
        
class DogReportCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DogReport
        fields = ["dog","original_image","description", "location_name"]
        
        