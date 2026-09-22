from rest_framework import serializers
from .models import VaccinationRecord

class VaccinationRecordModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VaccinationRecord
        fields = '__all__'