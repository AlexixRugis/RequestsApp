from django.db import models
from .RepairRequest import *
from app.models.employees.Employee import *

class RepairTask(models.Model):
    request = models.OneToOneField(RepairRequest, on_delete=models.CASCADE, related_name="task")
    executor = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="tasks")

    status_photo = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    is_completed = models.BooleanField(default=False)