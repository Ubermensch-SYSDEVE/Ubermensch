# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bir_certificate',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='order',
            name='dole_certification',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='order',
            name='org_chart',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='order',
            name='sec_registration_form',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='order',
            name='sss_certificate',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='order',
            name='vendor_application',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
