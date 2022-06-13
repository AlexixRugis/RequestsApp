from django.db import models

from app.models.repair_requests.RepairTask import *
from .RepairPart import *

class RepairPartRequest(models.Model):
    part = models.ForeignKey(RepairPart, on_delete=models.CASCADE)
    task = models.ForeignKey(RepairTask, on_delete=models.CASCADE, related_name="parts")
    amount = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.part}\nКоличество:{self.amount}\nСтатус: {self.is_completed}"