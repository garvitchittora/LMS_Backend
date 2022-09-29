from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint
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


class Class(models.Model):
    """
    Contains information of a class. A unique class is identified by a 
    number from 1-12 (or LKG, UKG, Nursery, etc.) and a section (A, B, C, etc.)
    """
    classname = models.CharField(_("class name"), max_length=10)
    section = models.CharField(_("section"), max_length=10)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["classname", "section"], name="class_unique_constraint"
            )
        ]
    
    def __str__(self) -> str:
        return f"{self.classname} {self.section}"
