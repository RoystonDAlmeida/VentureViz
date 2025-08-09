from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from .views import analyze_domain
from analyzer.views import analyze_domain

def health_check(request):
    """
        @Description:
            Health check endpoint
        @Args:
            request:- The HTTP request object.
        @Returns:
            JsonResponse:- A JSON response indicating the service is healthy.
    """

    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('', health_check, name="health_check"),
    path("admin/", admin.site.urls),
    path("analyze", analyze_domain, name="analyze"),
]