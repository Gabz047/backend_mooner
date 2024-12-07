# Generated by Django 5.1.2 on 2024-12-07 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_rename_secure_url_document_url'),
        ('usuario', '0002_usuario_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='background_dark_color',
            field=models.CharField(max_length=7, null='#000000'),
            preserve_default='#000000',
        ),
        migrations.AddField(
            model_name='usuario',
            name='background_image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='background', to='uploader.image'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='background_light_color',
            field=models.CharField(max_length=7, null='#000000'),
            preserve_default='#000000',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='perfil',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to='uploader.image'),
        ),
    ]
