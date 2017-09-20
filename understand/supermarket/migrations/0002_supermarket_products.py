# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-18 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('supermarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supermarket',
            name='products',
            field=models.ManyToManyField(related_name='supermaket_products', to='products.Product'),
        ),
    ]
