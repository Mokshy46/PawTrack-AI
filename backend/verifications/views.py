from .serializers import VerificationSubmissionModelSerialzer
from .models import VerificationSubmission
from rest_framework.generics import CreateAPIView



class VerificationSubmissionCreateAPIView(CreateAPIView):
    queryset = VerificationSubmission.objects.all()
    serializer_class = VerificationSubmissionModelSerialzer


