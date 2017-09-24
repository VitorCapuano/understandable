from brazilnum.cnpj import validate_cnpj
from django.conf import settings
from django.db import models


class Partner(models.Model):
    social_reason = models.CharField(max_length=100, null=False)
    cnpj = models.CharField(validators=[validate_cnpj], blank=True, max_length=14)
    city = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    address = models.CharField(max_length=100, blank=True, verbose_name='Endereço')
    cep = models.CharField(max_length=8, blank=False, verbose_name='Cep')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_partner')

    def clean_fields(self, exclude=None):
        if not validate_cnpj(self.cnpj):
            raise Exception("Invalid CNPJ")
        super(Partner, self).save()
