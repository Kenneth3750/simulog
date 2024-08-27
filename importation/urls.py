from django.contrib import admin
from django.urls import path

from .views import international_freight, policy, port_operator

urlpatterns = [
    path('international_freight/', international_freight),
    path('policy/', policy),
    path('port_operator/', port_operator)
]