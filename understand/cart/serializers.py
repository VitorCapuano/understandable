from django.conf import settings
from rest_framework import serializers

from cart.models import Cart
from products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    supermarket = serializers.CharField(source='supermarket.name')
    user = serializers.CharField(source='user.username')
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'products', 'total', 'finish', 'supermarket',)
