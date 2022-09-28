from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from students.models import Student

User = get_user_model()


class Subject(models.Model):
    """
    Contains information of a subject such as title, description, etc.
    """
    title = models.CharField(_("title"), max_length=100, unique=True)
    description = models.TextField(_("description"), blank=True)
    teachers = models.ManyToManyField(User, related_name="subjects")
    students = models.ManyToManyField(Student, related_name="subjects")

    def __str__(self) -> str:
        return self.title
