# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_billingstatement_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingstatement',
            name='percentage',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]
