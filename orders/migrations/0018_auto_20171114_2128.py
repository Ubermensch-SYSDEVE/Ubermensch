# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 13:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_inspectorreport_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectorreport',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]