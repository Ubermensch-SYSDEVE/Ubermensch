# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 03:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20171127_2258'),
        ('orders', '0066_auto_20171127_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('report_progress', models.TextField()),
                ('generated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]
