from django.db import models
from .PartCategory import PartCategory

class RepairPart(models.Model):
    name = models.CharField(max_length=150)
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(PartCategory, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name}\nВ наличии: {self.amount}\nЦена: {self.price} рублей"