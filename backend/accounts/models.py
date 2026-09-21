import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        CIVILIAN = "CIVILIAN", "Civilian"
        GOVERNMENT = "GOVERNMENT", "Government"
        ADMIN = "ADMIN", "Admin"

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    email = models.EmailField(unique=True)

    role = models.CharField(max_length=20,choices=Role.choices,default=Role.CIVILIAN)

    phone_number = models.CharField(max_length=20,blank=True)

    organization = models.CharField(max_length=255,blank=True,help_text="Government department or organization.")

    employee_id = models.CharField( max_length=100, unique=True, null=True, blank=True, help_text="Government employee/official ID.")

    is_verified = models.BooleanField( default=False, help_text="Whether the account has been verified.")

    created_at = models.DateTimeField( auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email