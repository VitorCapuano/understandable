from rest_framework import serializers

from supermarket.models import Supermarket


class ProductSupermarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supermarket
        fields = ('name',)
