from rest_framework import serializers

from partner.models import Partner


class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('social_reason', 'cnpj', 'city', 'address', 'cep')
