# Generated by Django 5.1.2 on 2024-11-08 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='url',
            new_name='secure_url',
        ),
    ]
