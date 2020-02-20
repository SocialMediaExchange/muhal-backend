# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-20 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0012_auto_20200220_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='country',
            field=models.CharField(choices=[('lb', 'Lebanon'), ('jo', 'Jordan'), ('other', 'Other')], max_length=100, verbose_name='country'),
        ),
    ]
