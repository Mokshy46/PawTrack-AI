import uuid

from django.conf import settings
from django.db import models


class VaccinationRecord(models.Model):
    class VaccineType(models.TextChoices):
        RABIES = "RABIES", "Rabies"
        OTHER = "OTHER", "Other"

    class Status(models.TextChoices):
        SUBMITTED = "SUBMITTED", "Submitted"
        UNDER_VERIFICATION = "UNDER_VERIFICATION", "Under Verification"
        VERIFIED = "VERIFIED", "Verified"
        FLAGGED = "FLAGGED", "Flagged"
        REJECTED = "REJECTED", "Rejected"

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    report = models.OneToOneField("reports.DogReport",on_delete=models.CASCADE,related_name="vaccination")

    dog = models.ForeignKey("dogs.Dog",on_delete=models.CASCADE,related_name="vaccinations")

    administered_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name="vaccinations_administered")

    vaccine_type = models.CharField(max_length=20,choices=VaccineType.choices,default=VaccineType.RABIES)

    vaccine_name = models.CharField(max_length=100,blank=True)

    batch_number = models.CharField(max_length=100,blank=True)

    evidence_image = models.ImageField(upload_to="vaccinations/evidence/")

    administered_at = models.DateTimeField(auto_now_add=True)

    latitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)

    longitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)

    notes = models.TextField(blank=True)

    status = models.CharField(max_length=30,choices=Status.choices,default=Status.SUBMITTED)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-administered_at"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["administered_at"]),
        ]

    def __str__(self):
        return f"{self.dog.tag_id} - {self.vaccine_type}"
    
    
    
class VaccinationAIAnalysis(models.Model):
    vaccination = models.OneToOneField(
        "VaccinationRecord",
        on_delete=models.CASCADE,
        related_name="ai_analysis"
    )

    dog_detected = models.BooleanField(default=False)

    ear_tag_detected = models.BooleanField(default=False)

    ear_tag_number = models.CharField(
        max_length=100,
        blank=True
    )

    ear_tag_readable = models.BooleanField(default=False)

    image_quality = models.CharField(
        max_length=20,
        blank=True
    )

    issues = models.JSONField(
        default=list,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AI Analysis - {self.vaccination.dog.tag_id}"