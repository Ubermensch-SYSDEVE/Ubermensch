# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-25 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0046_auto_20171123_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Contract', max_length=100),
        ),
    ]
