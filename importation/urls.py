from django.contrib import admin
from django.urls import path

from .views import international_freight

urlpatterns = [
    path('international_freight/', international_freight)
]