import uuid

from django.db import models


class Dog(models.Model):
    class Sex(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        UNKNOWN = "UNKNOWN", "Unknown"

    class VaccinationStatus(models.TextChoices):
        UNKNOWN = "UNKNOWN", "Unknown"
        UNVACCINATED = "UNVACCINATED", "Unvaccinated"
        VACCINATED = "VACCINATED", "Vaccinated"

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    tag_id = models.CharField(max_length=50,unique=True,editable=False)

    name = models.CharField(max_length=100,blank=True)

    sex = models.CharField(max_length=10,choices=Sex.choices,default=Sex.UNKNOWN)

    estimated_age = models.PositiveSmallIntegerField(null=True,blank=True,help_text="Estimated age in years.")

    breed = models.CharField(max_length=100,blank=True)

    color = models.CharField(max_length=100,blank=True)

    identifying_features = models.TextField(blank=True,help_text="Distinctive physical characteristics.")

    vaccination_status = models.CharField(max_length=20, choices=VaccinationStatus.choices, default=VaccinationStatus.UNKNOWN)

    latitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)

    longitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)

    first_seen_at = models.DateTimeField(auto_now_add=True)

    last_seen_at = models.DateTimeField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.tag_id:
            self.tag_id = f"DOG-{uuid.uuid4().hex[:8].upper()}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.tag_id