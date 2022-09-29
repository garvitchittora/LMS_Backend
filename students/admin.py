from django.contrib import admin

from students.models import Guardian, Student


@admin.register(Guardian)
class GuardianAdmin(admin.ModelAdmin):
    """
    Configuration for the handling the Guardian instances in the admin site.
    """
    model = Guardian
    list_display = ("id", "name", "phone_number", "email")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """
    Configuration for the handling the Student instances in the admin site.
    """
    models = Student
    list_display = ("enrollment_id", "class_section", "name", "phone_number", "email")
