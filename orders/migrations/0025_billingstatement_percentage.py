# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0024_auto_20171116_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingstatement',
            name='percentage',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
    ]