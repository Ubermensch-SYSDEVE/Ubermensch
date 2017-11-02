# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171029_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
                ('contact_first_name', models.CharField(max_length=50)),
                ('contact_last_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
