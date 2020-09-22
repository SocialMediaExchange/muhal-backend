# Generated by Django 3.0.7 on 2020-09-21 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('lebanon', 'Lebanon'), ('jordan', 'Jordan'), ('other', 'Other')], max_length=10, verbose_name='country')),
                ('plaintiff', models.CharField(max_length=200, verbose_name='plaintiff')),
                ('defendant', models.CharField(max_length=200, verbose_name='defendant')),
                ('what_happened', models.TextField(verbose_name='What happened')),
                ('notes', models.TextField(verbose_name='Our notes')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last modified')),
                ('processed', models.BooleanField(default=False, verbose_name='Processed?')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
    ]