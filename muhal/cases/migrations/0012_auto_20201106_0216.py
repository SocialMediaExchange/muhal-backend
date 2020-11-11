# Generated by Django 3.0.7 on 2020-11-06 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0011_auto_20201009_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defendant',
            name='citizenship',
            field=models.CharField(choices=[('lebanon', 'Lebanese'), ('jordan', 'Jordanian'), ('syria', 'Syrian'), ('palestine', 'Palestine'), ('stateless', 'Stateless'), ('unknown', 'Unknown'), ('other', 'Other')], max_length=10, verbose_name='citizenship'),
        ),
        migrations.AlterField(
            model_name='judge',
            name='kaza',
            field=models.CharField(blank=True, choices=[('Lebanon', (('Akkar', 'Akkar'), ('Minieh-Danieh', 'Minieh-Danieh'), ('Baalbeck', 'Baalbeck'), ('Hermel', 'Hermel'), ('Beirut', 'Beirut'), ('Rachiaya', 'Rachiaya'), ('West Bekaa', 'West Bekaa'), ('Zahleh', 'Zahleh'), ('Aley', 'Aley'), ('Baabda', 'Baabda'), ('Batroun', 'Batroun'), ('Chouf', 'Chouf'), ('El Metn', 'El Metn'), ('Jezzine', 'Jezzine'), ('Jubail', 'Jubail'), ('Kasrouane', 'Kasrouane'), ('Bint Jbayl', 'Bint Jbayl'), ('Hasbaya', 'Hasbaya'), ('Marjaayoun', 'Marjaayoun'), ('Nabatiyeh', 'Nabatiyeh'), ('Batroun', 'Batroun'), ('Bcharre', 'Bcharre'), ('Koura', 'Koura'), ('Minieh-Danieh', 'Minieh-Danieh'), ('Tripoli', 'Tripoli'), ('Zgharta', 'Zgharta'), ('Jezzine', 'Jezzine'), ('Nabatiyeh', 'Nabatiyeh'), ('Saida', 'Saida'), ('Sour', 'Sour'))), ('Jordan', (('Irbid', 'Irbid'), ('Ajloun', 'Ajloun'), ('Jerash', 'Jerash'), ('Mafraq', 'Mafraq'), ('Balqa', 'Balqa'), ('Amman', 'Amman'), ('Zarqa', 'Zarqa'), ('Madaba', 'Madaba'), ('Karak', 'Karak'), ('Tafilah', 'Tafilah'), ('Ma’an', 'Ma’an'), ('Aqaba', 'Aqaba')))], max_length=20, null=True, verbose_name='kaza'),
        ),
    ]