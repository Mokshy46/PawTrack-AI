from .models import VaccinationRecord,VaccinationAIAnalysis
from .serializers import VaccinationRecordModelSerializer
from .permissions import IsGovtOfficial
from ai.services.vaccination_verification import analyze_django_image
from rest_framework.generics import CreateAPIView,ListAPIView
from django.shortcuts import get_object_or_404
from dogs.models import Dog

class VaccinationRecordCreateAPIView(CreateAPIView):
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordModelSerializer
    permission_classes = [IsGovtOfficial]
    
    def perform_create(self, serializer):
      

        vaccination = serializer.save(
           
            administered_by=self.request.user
        )
        
        ai_result = analyze_django_image(
            vaccination.evidence_image
        )

        VaccinationAIAnalysis.objects.create(
            vaccination=vaccination,
            dog_detected=ai_result["dog_detected"],
            ear_tag_detected=ai_result["ear_tag_detected"],
            ear_tag_number=ai_result["ear_tag_number"],
            ear_tag_readable=ai_result["ear_tag_readable"],
            image_quality=ai_result["image_quality"],
            issues=ai_result["issues"],
        )
        
        

class VaccinationRecordListAPIView(ListAPIView):
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordModelSerializer


