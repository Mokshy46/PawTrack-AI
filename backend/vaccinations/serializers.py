from rest_framework import serializers
from .models import VaccinationRecord

class VaccinationRecordModelSerializer(serializers.ModelSerializer):
    
    administered_by_username = serializers.CharField(source = "administered_by.first_name", read_only = True)
    
    class Meta:
        model = VaccinationRecord
        fields = [
            "dog",
            "report",
            "vaccine_type",
            "vaccine_name",
            "batch_number",
            "evidence_image",
            "administered_at",
            "latitude",
            "longitude",
            "notes",
            "status",
            "administered_by",
            "administered_by_username",
        ]