from django.db import models

class Region(models.Models):
    name = models.CharField(max_length=50)

class Fruits(models.Models):
    name = models.CharField(max_length=25)
    # o segundo argumento é para evitar a remoção manual
    origin = models.ForeignKey(to=Region, on_delete=models.CASCADE)
