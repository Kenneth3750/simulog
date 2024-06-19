from django.contrib import admin
from django.urls import path
from .views import netWeight

urlpatterns = [
    path('', netWeight),
]
