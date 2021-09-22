# Generated by Django 3.0.7 on 2021-08-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0015_auto_20201123_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='country',
            field=models.CharField(choices=[('lebanon', 'Lebanon'), ('jordan', 'Jordan'), ('tunisia', 'Tunisia'), ('other', 'Other')], max_length=10, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='defendant',
            name='citizenship',
            field=models.CharField(choices=[('lebanon', 'Lebanese'), ('jordan', 'Jordanian'), ('tunis', 'Tunisian'), ('syria', 'Syrian'), ('palestine', 'Palestine'), ('stateless', 'Stateless'), ('unknown', 'Unknown'), ('other', 'Other')], max_length=10, verbose_name='citizenship'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='legal_entity',
            field=models.CharField(choices=[('Lebanon', (('publications', 'Publications court'), ('cassation', 'Cassation court'), ('appeals', 'Appellant court'), ('criminal', 'Criminal court'), ('military police', 'Military police centre'), ('army intel', 'Army Intelligence Branch'), ('military court', 'Military court'), ('state security', 'State security apparatus'), ('justice palace', 'Palace of Justice'), ('criminal investigations', 'Central bureau of criminal investigations'), ('public prosecutor', 'Executive public prosecutor'), ('general security', 'General security'))), ('Jordan', (('jo magistrate', 'Magistrate’s Courts'), ('jo first instance', 'Courts of First Instance'), ('jo appeal', 'Courts of Appeal'), ('jo cessation', 'Courts of Cassation'), ('jo administrative', 'Administrative court'), ('jo constitutional', 'Constitutional court'), ('jo major felonies', 'Major Felonies Court'), ('jo state security', 'State Security Court'))), ('Tunisia', (('tn cessation', 'Court of Cassation'), ('tn appeal', 'Court of Appeal'), ('tn first instance', 'Courts of First Instance '), ('tn military appeal', 'Military Court of Appeal'), ('tn military first instance', 'Military Court of First Instance')))], max_length=40, verbose_name='legal entity'),
        ),
    ]