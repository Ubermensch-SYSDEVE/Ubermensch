# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20171102_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='selling_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='unit_cost',
        ),
    ]
