# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-27 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0057_billingstatement_generated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingstatement',
            name='generated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
    ]