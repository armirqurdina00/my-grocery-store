from django.db import models
from markets.models import Market

class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class MarketProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='market_products')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        full_str = self.product.name + " - " + self.market.name
        return full_str