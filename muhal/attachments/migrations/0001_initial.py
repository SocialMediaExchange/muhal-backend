# Generated by Django 3.0.6 on 2020-06-01 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, verbose_name='label')),
                ('label_ar', models.CharField(max_length=100, null=True, verbose_name='label')),
                ('label_en', models.CharField(max_length=100, null=True, verbose_name='label')),
                ('file', models.FileField(upload_to='attachments/', verbose_name='file')),
                ('public', models.BooleanField(default=True, verbose_name='public')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'attachment',
                'verbose_name_plural': 'attachments',
            },
        ),
    ]
