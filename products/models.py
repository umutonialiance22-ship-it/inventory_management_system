from django.db import models
from suppliers.models import Supplier

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    low_stock_threshold=models.IntegerField(default=10)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
