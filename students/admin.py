from django.contrib import admin

from students.models import Guardian


@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    """
    Configuration for the handling the Guardian instances in the admin site.
    """
    model = Guardian
    list_display = ("id", "name", "phone_number", "email")
