from django.db import models
from pallets.models import Pallet


class Containers(models.Model):
    name = models.CharField(max_length=100)
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    weight = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.name
    
class ContainerPalletsPosition(models.Model):
    pallet_id = models.ForeignKey(Pallet, on_delete=models.CASCADE)
    container_id = models.ForeignKey(Containers, on_delete=models.CASCADE)
    position_1 = models.CharField(max_length=200)
    position_2 = models.CharField(max_length=200)
    position_3 = models.CharField(max_length=200)


