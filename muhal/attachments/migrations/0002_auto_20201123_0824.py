# Generated by Django 3.0.7 on 2020-11-23 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to='media/', verbose_name='file'),
        ),
    ]