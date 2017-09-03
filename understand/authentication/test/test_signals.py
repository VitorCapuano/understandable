import re
from unittest import TestCase

from django.conf import settings
from model_mommy import mommy

from rest_framework.authtoken.models import Token


class TestSignals(TestCase):

    def setUp(self):
        self.user = mommy.make(settings.AUTH_USER_MODEL)

    def test_iana(self):
        token = Token.objects.get(user=self.user)
        assert len(token.key) == 40


