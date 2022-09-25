from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.forms import UserCreationForm
from users.models import User


class UserAdmin(BaseUserAdmin):
    model = User
    add_form = UserCreationForm
    fieldsets = (
        *BaseUserAdmin.fieldsets,
        (
            "Roles",
            {"fields": ("is_admin", "is_teacher", "is_accountant")},
        ),
        (
            "General Details",
            {
                "fields": (
                    "phone_number", 
                    "address", 
                    "city", 
                    "nationality", 
                    "social_category", 
                    "designation", 
                    "annual_income", 
                    "image",
                )
            },
        )
    )

admin.site.register(User, UserAdmin)
