# Generated by Django 3.1.14 on 2024-10-06 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intento1',
            old_name='email',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='intento1',
            old_name='archivo',
            new_name='txt',
        ),
    ]
