from django.contrib import admin
from django.urls import path

from .views import international_freight, policy, port_operator, mobilization_and_manipulation, inspection, port_facility

urlpatterns = [
    path('international_freight/', international_freight),
    path('policy/', policy),
    path('port_operator/', port_operator),
    path('mobilization_and_manipulation/', mobilization_and_manipulation),
    path('inspection/', inspection),
    path('port_facility/', port_facility),

]