from django.contrib import admin
from django.urls import path

from .views import international_freight, policy, port_operator, mobilization_and_manipulation, inspection, port_facility, customs_broker
from .views import weight, volume, insurance, administrative_costs, other_costs

urlpatterns = [
    path('international_freight/', international_freight),
    path('policy/', policy),
    path('port_operator/', port_operator),
    path('mobilization_and_manipulation/', mobilization_and_manipulation),
    path('inspection/', inspection),
    path('port_facility/', port_facility),
    path('customs_broker/', customs_broker),
    path('weight/', weight),
    path('volume/', volume),
    path('insurance/', insurance),
    path('administrative_costs/', administrative_costs),
    path('other_costs/', other_costs)
]