import uuid
from uuid import uuid4

from django.db import models

from django.conf import settings


class Supermarket(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    city = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    address = models.CharField(max_length=100, blank=True, verbose_name='Endereço')
    cep = models.CharField(max_length=8, blank=False, verbose_name='Cep')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    price = models.DecimalField(decimal_places=2, max_digits=12, blank=False, verbose_name='Preço')
    slug = models.SlugField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    supermarket = models.ManyToManyField(Supermarket, related_name='supermarket')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='product')

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user')
    products = models.ManyToManyField(Product, related_name='products')
    finish = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.user.username
