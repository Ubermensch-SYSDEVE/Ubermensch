# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20171101_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_accredited',
            field=models.BooleanField(default=False),
        ),
    ]
