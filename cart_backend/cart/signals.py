
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Product, Discount

@receiver(post_migrate)
def create_initial_data(sender, **kwargs):
    if sender.name == 'cart':
        if not Product.objects.exists():
            a = Product.objects.create(name='A', price=50)
            b = Product.objects.create(name='B', price=30)
            c = Product.objects.create(name='C', price=20)
            d = Product.objects.create(name='D', price=15)

            Discount.objects.create(product=a, quantity=3, discounted_price=130)
            Discount.objects.create(product=b, quantity=2, discounted_price=45)
