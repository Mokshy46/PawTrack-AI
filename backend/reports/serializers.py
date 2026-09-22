from rest_framework import serializers
from .models import DogReport


class DogReportModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DogReport
        fields = "__all__"
        