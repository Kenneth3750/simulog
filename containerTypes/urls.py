from django.contrib import admin
from django.urls import path
from .views import getContainer, getContainerPosition, totalContainers

urlpatterns = [
    path('', getContainer),
    path('<int:id>', getContainer),
    path('positions/', getContainerPosition),
    path('total/', totalContainers),
]
