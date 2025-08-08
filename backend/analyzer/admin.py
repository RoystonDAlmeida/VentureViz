from django.contrib import admin
from .models import AnalysisResult, UserRequestLog

# The @admin.register() decorator is a clean way to register a model with the admin site.
@admin.register(AnalysisResult)
class AnalysisResultAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the AnalysisResult model.
    """

    # Specifies the columns to display in the admin list view for AnalysisResult objects.
    list_display = ("domain", "created_at")

    # Makes the 'created_at' field non-editable in the admin form.
    readonly_fields = ("created_at",)

    # Sets the default sorting for the list view. The '-' indicates descending order,
    # so the newest results will be shown first.
    ordering = ("-created_at",)

@admin.register(UserRequestLog)
class UserRequestLogAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the UserRequestLog model.
    """

    list_display = ("ip_address", "timestamp")
    ordering = ("-timestamp",)