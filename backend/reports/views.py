from .serializers import DogReportModelSerializer,DogReportCreateSerializer
from .models import DogReport
from rest_framework.generics import CreateAPIView,ListAPIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser,FormParser

User = get_user_model()


class DogReportListAPIView(ListAPIView):
    queryset = DogReport.objects.all()
    serializer_class = DogReportModelSerializer
    
    def get_queryset(self):
        reported_user = User.objects.get(email = self.request.user)
        return DogReport.objects.filter(reported_by = reported_user)
    



class DogReportCreateAPIView(CreateAPIView):
    queryset = DogReport.objects.all()
    serializer_class = DogReportCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def perform_create(self, serializer):
        
        serializer.save(reported_by = self.request.user)
        
    def create(self, request, *args, **kwargs):
        print("DATA:", request.data)
        print("FILES:", request.FILES)
        return super().create(request, *args, **kwargs)
            
       
