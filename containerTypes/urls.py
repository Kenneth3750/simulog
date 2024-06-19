from django.contrib import admin
from django.urls import path
from .views import ContainerView

urlpatterns = [
    path('', ContainerView.as_view()),
    path('<int:id>', ContainerView.as_view()),
]
