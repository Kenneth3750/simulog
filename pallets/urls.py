from django.contrib import admin
from django.urls import path
from .views import getPallets, getPositions, totalPallets, palletCost, totalPalletCost

urlpatterns = [
    path('', getPallets),
    path('<int:id>', getPallets),
    path('positions/', getPositions),
    path('total/', totalPallets),
    path('cost/', palletCost),
    path('totalcost/', totalPalletCost),
]
