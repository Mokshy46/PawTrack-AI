import uuid

from django.db import models


class VerificationSubmission(models.Model):
    class Decision(models.TextChoices):
        PENDING = "PENDING", "Pending"
        VERIFIED = "VERIFIED", "Verified"
        FLAGGED = "FLAGGED", "Flagged"
        REVIEW = "REVIEW", "Requires Review"
        FAILED = "FAILED", "Failed"

    class ImageIntegrity(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PASS = "PASS", "Pass"
        SUSPICIOUS = "SUSPICIOUS", "Suspicious"
        FAILED = "FAILED", "Failed"

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    vaccination = models.OneToOneField("vaccinations.VaccinationRecord",on_delete=models.CASCADE,related_name="verification")

    # AI verification signals

    dog_match_score = models.FloatField(null=True,blank=True,help_text="Similarity score between the original and evidence dog images.")

    image_integrity_score = models.FloatField(
        null=True,
        blank=True,
        help_text="Estimated image integrity score.")

    image_integrity = models.CharField(max_length=20,choices=ImageIntegrity.choices,default=ImageIntegrity.PENDING)

    metadata_consistent = models.BooleanField(null=True,blank=True)

    duplicate_detected = models.BooleanField(null=True,blank=True)

    # Final AI decision

    decision = models.CharField(max_length=20,choices=Decision.choices,default=Decision.PENDING)

    confidence_score = models.FloatField(null=True,blank=True)

    explanation = models.TextField(blank=True,help_text="Human-readable explanation of the verification result.")

    # Processing information

    model_name = models.CharField(max_length=100,blank=True)

    model_version = models.CharField(max_length=50,blank=True)

    processing_time_ms = models.PositiveIntegerField(null=True,blank=True)

    error_message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    completed_at = models.DateTimeField(null=True,blank=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["decision"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"Verification {self.id} - {self.decision}"