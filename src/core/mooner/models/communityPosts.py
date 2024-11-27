from django.db import models

from core.usuario.models import Usuario
from . import Song, Community
from core.uploader.models import Image

class CommunityPosts(models.Model):
    title = models.CharField(null=False, max_length=160)
    description = models.TextField(null=True, max_length=850)
    autor = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    cover = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='+')
    songs = models.ForeignKey(Song, on_delete=models.PROTECT, null=True, blank=True, default=None)
    community = models.ForeignKey(Community, on_delete=models.PROTECT, null=True)
    likes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title