from .models import VaccinationRecord
from .serializers import VaccinationRecordModelSerializer
from rest_framework.generics import CreateAPIView



class VaccinationRecordCreateAPIView(CreateAPIView):
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordModelSerializer


