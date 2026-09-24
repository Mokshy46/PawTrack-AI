from .models import VaccinationRecord
from .serializers import VaccinationRecordModelSerializer
from .permissions import IsGovtOfficial
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404
from dogs.models import Dog

class VaccinationRecordCreateAPIView(CreateAPIView):
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordModelSerializer
    permission_classes = [IsGovtOfficial]
    
    def perform_create(self, serializer):
      

        serializer.save(
           
            administered_by=self.request.user
        )