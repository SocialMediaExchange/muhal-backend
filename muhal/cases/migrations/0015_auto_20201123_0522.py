# Generated by Django 3.0.7 on 2020-11-23 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0014_auto_20201115_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='cases.Case'),
        ),
    ]
