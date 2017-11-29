# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_profile_email'),
        ('maintenance', '0002_auto_20171108_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='TroubleReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trouble_report_no', models.CharField(default='na', max_length=10)),
                ('date_requested', models.DateField()),
                ('date_created', models.DateField()),
                ('date_of_visit', models.DateField()),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('complaint', models.TextField(max_length=1500)),
                ('findings', models.TextField(max_length=1500)),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Profile')),
            ],
        ),
    ]