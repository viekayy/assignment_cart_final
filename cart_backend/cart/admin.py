from django.contrib import admin
from .models import Product, Discount

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'discounted_price']
    list_filter = ['product']
