from django.urls import path
from .views import VerificationSubmissionCreateAPIView

urlpatterns = [
    path('info/', VerificationSubmissionCreateAPIView.as_view(), name='info')
]
