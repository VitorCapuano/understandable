from django.db import models

from products.models import Product


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, related_name='product')

    def __str__(self):
        return self.name
