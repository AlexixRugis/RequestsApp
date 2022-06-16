from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class RepairRequest(models.Model):
    org_name = models.TextField()
    org_address = models.TextField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    org_phone = models.CharField(validators = [phoneNumberRegex], max_length = 16)

    name = models.CharField(max_length=200)
    description = models.TextField()
    desired_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.org_name})"
