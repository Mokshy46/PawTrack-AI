import uuid

from django.conf import settings
from django.db import models


class ActivityEvent(models.Model):
    class EventType(models.TextChoices):
        REPORT_CREATED = "REPORT_CREATED", "Report Created"
        REPORT_UPDATED = "REPORT_UPDATED", "Report Updated"
        CASE_ASSIGNED = "CASE_ASSIGNED", "Case Assigned"
        VACCINATION_SUBMITTED = "VACCINATION_SUBMITTED", "Vaccination Submitted"
        VERIFICATION_STARTED = "VERIFICATION_STARTED", "Verification Started"
        VERIFICATION_COMPLETED = "VERIFICATION_COMPLETED", "Verification Completed"
        VERIFICATION_FLAGGED = "VERIFICATION_FLAGGED", "Verification Flagged"
        STATUS_CHANGED = "STATUS_CHANGED", "Status Changed"
        COMMENT_ADDED = "COMMENT_ADDED", "Comment Added"

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    event_type = models.CharField(max_length=50,choices=EventType.choices,)

    report = models.ForeignKey("reports.DogReport",on_delete=models.CASCADE,related_name="activities")

    actor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name="activity_events")

    description = models.TextField()

    metadata = models.JSONField(default=dict,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.event_type} - {self.report_id}"