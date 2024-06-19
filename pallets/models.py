from django.db import models


class Pallet(models.Model):
    name = models.CharField(max_length=100)
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    weight = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.name
    
# amr = Pallet(name="AMR", width=1.0, height=0.14, length=1.2, weight=14.0)
# amr.save()
# eur = Pallet(name="EUR", width=0.8, height=0.14, length=1.0, weight=12.0)
# eur.save()