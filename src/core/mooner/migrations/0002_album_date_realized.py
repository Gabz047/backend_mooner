# Generated by Django 5.0.7 on 2024-10-29 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='date_realized',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
