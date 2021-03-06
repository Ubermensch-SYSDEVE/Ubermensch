# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0054_order_has_contract_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='first_percentage',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='contract',
            name='second_percentage',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name='contract',
            name='third_percentage',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4),
        ),
    ]
