import uuid

from django.conf import settings
from django.db import models

# Create your models here.
from products.models import Product


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user')
    products = models.ManyToManyField(Product, related_name='productt')
    finish = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.user.username
