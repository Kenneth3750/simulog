from django.contrib import admin
from django.urls import path
from .views import verify_user

urlpatterns = [
    path('verify/', verify_user),
]
