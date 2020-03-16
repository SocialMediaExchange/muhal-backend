# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-13 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0022_auto_20200312_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='country',
        ),
        migrations.AddField(
            model_name='lawarticle',
            name='law',
            field=models.CharField(choices=[('publication', 'Publications law'), ('penal', 'Penal code'), ('electronic', 'Electronic affairs'), ('military', 'Military law'), ('other', 'Other')], default=None, null=True, max_length=10, verbose_name='law'),
            preserve_default=False,
        ),
    ]
