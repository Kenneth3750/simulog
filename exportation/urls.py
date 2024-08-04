from django.contrib import admin
from django.urls import path
from .views import exportation_price, weight, volume, insurance, inspection, mobilization_and_manipulation, customs_broker, administrative_costs, other_costs
from .views import port_facility


urlpatterns = [
    path('total/', exportation_price),
    path('weight/', weight),
    path('volume/', volume),
    path('insurance/', insurance),
    path('inspection/', inspection),
    path('mobilization_and_manipulation/', mobilization_and_manipulation),
    path('customs_broker/', customs_broker),
    path('administrative_costs/', administrative_costs),
    path('other_costs/', other_costs),
    path('port_facility/', port_facility)
]  