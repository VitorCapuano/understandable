import uuid

from decimal import Decimal
from django.conf import settings
from django.db import models

# Create your models here.
from products.models import Product
from supermarket.models import Supermarket


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user')
    products = models.ManyToManyField(Product, related_name='cart_prod')
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    finish = models.BooleanField(default=False, null=False)
    supermarket = models.OneToOneField(Supermarket, related_name='supermarket_cart')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        total = Decimal(0)
        for product in self.products.values_list():
            cart_products = CartProducts.objects.filter(cart=self.pk)
            cart_products = cart_products.get(product=product)
            total += cart_products.total
        self.total = total
        super().save(*args, **kwargs)


class CartProducts(models.Model):
    cart = models.UUIDField()
    product = models.OneToOneField(Product, related_name='cart_product')
    qtd = models.IntegerField()
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total = self.qtd * self.product.price
        super().save(*args, **kwargs)
