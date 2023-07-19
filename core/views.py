from django.shortcuts import render, redirect
from products.models import Product, MarketProduct
from markets.models import Market
from shopping_cart.models import ShoppingCartItem

def index(request):
    cart_items = ShoppingCartItem.objects.all()

    lowest_market_price = {}

    if cart_items:
        cart_product_ids = map(lambda cart_item: cart_item.product_id, cart_items)
        market_products = MarketProduct.objects.filter(product_id__in=cart_product_ids)
        
        market_products_by_market = {}
        for market_product in market_products:
            market_id = market_product.market_id
            # import json
            # market_products_by_market.setdefault(market_id, []).append(market_product)
            if market_id not in market_products_by_market:
                market_products_by_market[market_id] = []
            market_products_by_market[market_id].append(market_product)

        for market_id, market_products in market_products_by_market.items():
            if len(market_products) == len(cart_items):
                # total_market_price = sum(market_product.price for market_product in market_products)
                total_market_price = 0
                for market_product in market_products:
                    total_market_price += market_product.price
                if ("price" not in lowest_market_price) or total_market_price < lowest_market_price["price"]:
                    lowest_market_price = {"market_id": market_product.market_id, "price": total_market_price}
        
        if "market_id" in lowest_market_price:
             print(lowest_market_price['market_id'])
             lowest_market_price["market"] = Market.objects.get(pk=lowest_market_price['market_id'])

    products = Product.objects.all()

    context = {
        'products': products,
        'orders': cart_items,
        **lowest_market_price
    }

    return render(request, 'home.html', context)

def order(request, pk):
    product = Product.objects.get(id=pk)
    order = ShoppingCartItem(product=product)
    order.save()
    return redirect('home')

def delete(request, pk):
    order_to_delete = ShoppingCartItem(id=pk)
    order_to_delete.delete()
    return redirect('home')