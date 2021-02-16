from django.db import models


class Artykuly(models.Model):
    class Meta:
        verbose_name='Artykuły model'
    title = models.CharField(max_length=128, null=False, verbose_name='Tytuł artykułu xxx')
    description = models.CharField(max_length=255, null=True, verbose_name='Opis artykułu')

    def __str__(self):
        return self.title
