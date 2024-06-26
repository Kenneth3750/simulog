from django.contrib import admin
from django.urls import path
from .views import netWeight, totalVolumePerProduct, totalVolume, totalCostPerProduct, totalCost, totalTagPerProduct, totalTag

urlpatterns = [
    path('weight', netWeight),
    path('volume', totalVolumePerProduct),
    path('totalvolume', totalVolume),
    path('cost', totalCostPerProduct),
    path('totalcost', totalCost),
    path('tag', totalTagPerProduct),
    path('totaltag', totalTag)
]
