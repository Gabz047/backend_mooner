from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.uploader.models import Image
from core.usuario.managers import CustomUserManager

class Usuario(AbstractUser):
    username = None
    perfil = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None)
    email = models.EmailField(_("e-mail address"), unique=True)
    following = models.IntegerField(default=0, blank=True, null=True)
    is_artist = models.BooleanField(default=False, blank=True, null=True)
    token_verification = models.CharField(max_length=100, blank=True, null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]