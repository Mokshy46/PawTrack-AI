from .serializers import DogReportModelSerializer
from .models import DogReport
from rest_framework.generics import CreateAPIView



class DogReportCreateAPIView(CreateAPIView):
    queryset = DogReport.objects.all()
    serializer_class = DogReportModelSerializer


