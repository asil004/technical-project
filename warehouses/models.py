from django.db import models
from materials.models import Materials


class Warehouses(models.Model):
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, related_name='material_warehouse')
    reminder = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.material.name} {self.reminder} {self.price}"
