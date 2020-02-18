# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-18 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0010_auto_20200211_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='LawArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100, verbose_name='number')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('name_ar', models.CharField(max_length=100, null=True, verbose_name='name')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='bail',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='bail amount'),
        ),
        migrations.AddField(
            model_name='case',
            name='charge',
            field=models.TextField(blank=True, null=True, verbose_name='charge'),
        ),
        migrations.AddField(
            model_name='case',
            name='charged_using',
            field=models.ManyToManyField(to='cases.LawArticle', verbose_name='charged using law article'),
        ),
    ]
