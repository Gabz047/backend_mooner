# Generated by Django 5.0.7 on 2024-10-17 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooner', '0005_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='album',
            name='post_date',
            field=models.DateField(auto_now=True),
        ),
    ]
