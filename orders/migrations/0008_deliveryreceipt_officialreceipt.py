# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20171106_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OfficialReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]