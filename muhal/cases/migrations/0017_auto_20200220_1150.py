# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-20 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0016_auto_20200220_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='charged_using',
            field=models.ManyToManyField(blank=True, to='cases.LawArticle', verbose_name='charged using law article'),
        ),
    ]
