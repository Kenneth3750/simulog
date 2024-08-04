from django.contrib import admin
from django.urls import path
from .views import exportation_price, weight, volume, insurance, inspection, mobilization_and_manipulation


urlpatterns = [
    path('total/', exportation_price),
    path('weight/', weight),
    path('volume/', volume),
    path('insurance/', insurance),
    path('inspection/', inspection),
    path('mobilization_and_manipulation/', mobilization_and_manipulation),
]  