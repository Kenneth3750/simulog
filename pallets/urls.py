from django.contrib import admin
from django.urls import path
from .views import PalletsView

urlpatterns = [
    path('', PalletsView.as_view()),
    path('<int:id>', PalletsView.as_view()),
]
