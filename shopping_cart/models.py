from django.db import models
from products.models import Product

class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.product.name