# Generated by Django 5.0.7 on 2024-10-28 13:58

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, verbose_name='e-mail address')),
                ('following', models.IntegerField(blank=True, default=0, null=True)),
                ('is_artist', models.BooleanField(blank=True, default=False, null=True)),
                ('token_verification', models.CharField(blank=True, max_length=100, null=True)),
                ('premium', models.CharField(blank=True, choices=[('Eclipse', 'Eclipse'), ('Lua Nova', 'Lua Nova'), ('Apollo 8', 'Apollo 8'), ('Ano Lunar', 'Ano Lunar'), ('Lua Cheia', 'Lua Cheia')], default=None, max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('perfil', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='uploader.image')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('artistic_name', models.CharField(blank=True, max_length=100, null=True)),
                ('following', models.IntegerField(blank=True, default=0, null=True)),
                ('followers', models.IntegerField(blank=True, default=0, null=True)),
                ('instagram', models.URLField(blank=True, max_length=255, null=True)),
                ('youtube', models.URLField(blank=True, max_length=255, null=True)),
                ('twitter', models.URLField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
