# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20171102_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='unit_cost',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=10),
        ),
    ]
