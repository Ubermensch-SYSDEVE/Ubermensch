# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0067_progressreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='progressreport',
            name='title',
            field=models.CharField(default='', max_length=256),
        ),
    ]
