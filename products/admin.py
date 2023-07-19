from django.contrib import admin
from products.models import Product, MarketProduct
from markets.models import Market

admin.site.register(Product)
admin.site.register(MarketProduct)
admin.site.register(Market)
