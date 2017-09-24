from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
# from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tel = models.CharField(null=True, max_length=14)
    birth_date = models.DateField(null=True)
    cel = models.CharField(null=True, max_length=14)

    def __str__(self):
        return self.username
