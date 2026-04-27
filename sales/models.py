from django.db import models
from products.models import Product

# Create your models here.
class Sale(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    sale_date=models.DateField(auto_now_add=True)

    def __str__ (self):
        return f"{self.product} - {self.quantity}"
    

