# Generated by Django 3.0.7 on 2020-10-09 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0010_auto_20201006_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawarticle',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='lawarticle',
            name='name_ar',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='lawarticle',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='lawarticle',
            name='number',
            field=models.CharField(help_text='Prefix the number with article or articles, to make sure it renders as a complete sentence', max_length=100, verbose_name='number'),
        ),
    ]
