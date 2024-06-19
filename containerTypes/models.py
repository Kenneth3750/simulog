from django.db import models


class Containers(models.Model):
    name = models.CharField(max_length=100)
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    weight = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.name

