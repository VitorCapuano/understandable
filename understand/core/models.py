from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    price = models.DecimalField(decimal_places=2, max_digits=12, blank=False, verbose_name='Preço')
    slug = models.SlugField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)

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


class Supermarket(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    city = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    address = models.CharField(max_length=100, blank=True, verbose_name='Endereço')
    cep = models.CharField(max_length=8, blank=False, verbose_name='Cep')
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='products')

    def __str__(self):
        return self.name
