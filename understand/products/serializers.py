from rest_framework import serializers

from core.serializers import ProductSupermarketSerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    supermarket = ProductSupermarketSerializer(many=True, )

    class Meta:
        model = Product
        fields = ('name', 'supermarket', 'price', 'slug',)
