# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-10 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_accused'),
    ]

    operations = [
        migrations.AddField(
            model_name='accused',
            name='first_name_ar',
            field=models.CharField(max_length=40, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='accused',
            name='first_name_en',
            field=models.CharField(max_length=40, null=True, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='accused',
            name='last_name_ar',
            field=models.CharField(max_length=40, null=True, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='accused',
            name='last_name_en',
            field=models.CharField(max_length=40, null=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='accused',
            name='citizenship',
            field=models.CharField(choices=[('leb', 'Lebanese'), ('syr', 'Syrian'), ('non', 'Stateless'), ('other', 'Other')], max_length=6, verbose_name='citizenship'),
        ),
    ]