from django.contrib import admin
from django.urls import path
from .views import verify_user, users_list

urlpatterns = [
    path('verify/', verify_user),
    path('list/', users_list),
]
