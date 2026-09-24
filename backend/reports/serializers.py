from rest_framework import serializers
from .models import DogReport


class DogReportModelSerializer(serializers.ModelSerializer):
    
    reported_by_username = serializers.CharField( source = "reported_by.first_name", read_only = True)
    dog_tag = serializers.CharField(source = "dog.tag_id", read_only = True)
    
    class Meta:
        model = DogReport
        fields = [
            "id",
            "original_image",
            "description",
            "latitude",
            "longitude",
            "location_name",
            "status",
            "created_at",
            "updated_at",
            "resolved_at",
            "dog",
            "dog_tag",
            "reported_by",
            "reported_by_username",
            "assigned_to",
            
        ]
        
class DogReportCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DogReport
        fields = ["dog","original_image","description", "location_name"]
        
        