# Generated by Django 3.0.7 on 2020-10-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0008_auto_20200916_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='defendant',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='plaintiff',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='plaintiff',
            name='description_ar',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='plaintiff',
            name='description_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='plaintiff',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='plaintiff',
            name='first_name_ar',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='plaintiff',
            name='first_name_en',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='plaintiff',
            name='last_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='plaintiff',
            name='last_name_ar',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='plaintiff',
            name='last_name_en',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='last name'),
        ),
    ]