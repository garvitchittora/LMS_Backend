from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import UserCreationForm
from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    add_form = UserCreationForm
    list_display = ("username", "email", "name")
    search_fields = ("username", "name", "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info", 
            {
                "fields": (
                    "name",
                    "email",
                    "gender",
                    "phone_number", 
                    "address", 
                    "city", 
                    "nationality", 
                    "social_category", 
                    "designation", 
                    "annual_income", 
                    "image",
                )
            }
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        (
            "Roles",
            {"fields": ("is_admin", "is_teacher", "is_accountant")},
        ),
    )
