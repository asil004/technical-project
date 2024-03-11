from django.db import models
from product.models import Product
from materials.models import Materials


class ProductMaterials(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_materials')
    material = models.ForeignKey(Materials, on_delete=models.CASCADE, related_name='material_materials')
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.product} {self.material} {self.quantity}"
