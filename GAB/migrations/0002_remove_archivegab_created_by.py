# Generated by Django 5.0.1 on 2024-05-24 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GAB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivegab',
            name='created_by',
        ),
    ]
