from rest_framework import serializers

from core.serializers import ProductSupermarketSerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'slug',)
