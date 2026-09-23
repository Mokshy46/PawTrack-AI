import uuid

from django.conf import settings
from django.db import models


class DogReport(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ASSIGNED = "ASSIGNED", "Assigned"
        VACCINATION_SUBMITTED = (
            "VACCINATION_SUBMITTED",
            "Vaccination Submitted",
        )
        UNDER_VERIFICATION = (
            "UNDER_VERIFICATION",
            "Under Verification",
        )
        VERIFIED = "VERIFIED", "Verified"
        FLAGGED = "FLAGGED", "Flagged"
        RESOLVED = "RESOLVED", "Resolved"
        REJECTED = "REJECTED", "Rejected"

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    reference_id = models.CharField(max_length=50,unique=True,editable=False)

    dog = models.ForeignKey("dogs.Dog",on_delete=models.CASCADE,related_name="reports")

    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name="dog_reports")

    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name="assigned_dog_reports")

    original_image = models.ImageField(upload_to="reports/originals/")

    description = models.TextField(blank=True)

    latitude = models.DecimalField(max_digits=9,decimal_places=6, null= True, blank=True)

    longitude = models.DecimalField(max_digits=9,decimal_places=6, null= True, blank=True)

    location_name = models.CharField(max_length=255,blank=True)

    status = models.CharField(max_length=30,choices=Status.choices,default=Status.PENDING)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    resolved_at = models.DateTimeField(null=True,blank=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["latitude", "longitude"]),
            models.Index(fields=["created_at"]),
        ]

    def save(self, *args, **kwargs):
        if not self.reference_id:
            self.reference_id = f"PTR-{uuid.uuid4().hex[:8].upper()}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference_id