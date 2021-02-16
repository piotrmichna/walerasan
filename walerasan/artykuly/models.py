from django.db import models


class Artykuly(models.Model):
    title = models.CharField(max_length=128, null=False, verbose_name='Tytuł artykułu')
    description = models.CharField(max_length=255, null=True, verbose_name='Opis artykułu')
