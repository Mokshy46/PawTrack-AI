from rest_framework import serializers
from .models import VerificationSubmission

class VerificationSubmissionModelSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model = VerificationSubmission
        fields = "__all__"