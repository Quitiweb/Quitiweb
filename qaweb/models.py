from django.db import models

ZONA_MAX_LENGTH = 50

# Create your models here.
class Map(models.Model):
    Zona = models.CharField(max_length = ZONA_MAX_LENGTH)
    Latitud = models.FloatField()
    Longitud = models.FloatField()

    class Meta:
        verbose_name_plural = 'Mapa'

    def __str__(self):
        return self.title