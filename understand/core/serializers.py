from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class SupermarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supermarket
        fields = '__all__'


class ProductSupermarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supermarket
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    supermarket = ProductSupermarketSerializer(many=True, )

    class Meta:
        model = Product
        fields = ('name', 'supermarket', 'price', 'slug',)



