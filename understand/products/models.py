from django.db import models
from django.template.defaultfilters import slugify


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    price = models.DecimalField(decimal_places=2, max_digits=12, blank=False, verbose_name='Preço')
    slug = models.SlugField(max_length=40, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
