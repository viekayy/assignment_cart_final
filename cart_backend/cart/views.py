
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from django.template.loader import render_to_string
from .models import Product, Discount

@method_decorator(csrf_exempt, name='dispatch')
class CheckoutView(View):
    def get(self, request):
        return HttpResponse(render_to_string('checkout.html'))

    def post(self, request):
        body = json.loads(request.body)
        cart = body.get('cart', '')
        print(cart)
        item_counts = {}
        for item in cart:
            print()
            item_counts[item] = item_counts.get(item, 0) + 1
            print()
            print("item is ",item,"its count is ",  item_counts[item] )

        total_price = 0
        for item, count in item_counts.items():
            try:
                product = Product.objects.get(name=item)
            except Product.DoesNotExist:
                continue
            try:
                discount = Discount.objects.get(product=product)
                print()
                print("meri discount ki quantity hai ", discount)
                print("meri discount ki quantity hai ", discount.quantity)
                times_discount_applies = count // discount.quantity 
                remaining = count % discount.quantity 
                total_price += times_discount_applies * discount.discounted_price + remaining * product.price
            except Discount.DoesNotExist:
                print("count is not existing in discount")
                total_price += count * product.price

        return JsonResponse({'total_price': total_price})
