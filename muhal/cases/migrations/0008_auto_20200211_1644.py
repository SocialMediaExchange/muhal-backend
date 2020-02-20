# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-11 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0007_auto_20200211_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='case',
            name='summary',
            field=models.TextField(blank=True, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='case',
            name='defendants',
            field=models.ManyToManyField(blank=True, to='cases.Defendant', verbose_name='defendants'),
        ),
        migrations.AlterField(
            model_name='case',
            name='plaintiffs',
            field=models.ManyToManyField(blank=True, to='cases.Plaintiff', verbose_name='plaintiffs'),
        ),
    ]