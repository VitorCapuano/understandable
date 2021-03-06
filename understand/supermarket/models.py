from django.db import models


class Supermarket(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    city = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    address = models.CharField(max_length=100, blank=True, verbose_name='Endereço')
    cep = models.CharField(max_length=8, blank=False, verbose_name='Cep')
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('products.Product', related_name='supermaket_products')

    def __str__(self):
        return self.name
