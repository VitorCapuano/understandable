from brazilnum.cpf import validate_cpf
from django.conf import settings
from django.db import models


class Client(models.Model):
    cpf = models.CharField(validators=[validate_cpf], blank=True, max_length=11)
    city = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    address = models.CharField(max_length=100, blank=True, verbose_name='Endereço')
    cep = models.CharField(max_length=8, blank=False, verbose_name='Cep')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_client')

    def clean_fields(self, exclude=None):
        if not validate_cpf(self.cpf):
            raise Exception("Invalid CPF")
        super(Client, self).clean_fields()
