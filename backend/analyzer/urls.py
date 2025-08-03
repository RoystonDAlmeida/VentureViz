from django.urls import path
from .views import analyze_domain

urlpatterns = [
    path("analyze", analyze_domain, name="analyze"),
]