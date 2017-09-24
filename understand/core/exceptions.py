from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import ugettext_lazy as _


class HttpError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('Erro interno')
    default_code = 'Erro interno'


class ModelDoesNotFound(HttpError):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('Não existente')
    default_code = 'Modelo não existe'


class ValidationError(HttpError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Erro na validação dos dados')
    default_code = 'Erro de Validação do serializador'
