from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from students.utils import (
    GuardianStudentRelations,
    guardian_image_path,
    student_image_path,
)
from users.utils import GenderChoices


class Guardian(models.Model):
    """
    Stores information of the guardian/parent of a student.
    """

    name = models.CharField(_("name"), max_length=300, blank=True)
    relation = models.CharField(
        _("relation"),
        max_length=20,
        default=GuardianStudentRelations.RELATIVE,
        choices=GuardianStudentRelations.choices,
    )
    age = models.PositiveSmallIntegerField(_("age"), default=0)
    gender = models.CharField(
        _("gender"),
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
        max_length=15,
    )
    occupation = models.CharField(_("occupation"), blank=True, max_length=300)
    email = models.EmailField(_("email"), blank=True)
    phone_number = models.CharField(_("phone number"), blank=True, max_length=16)
    address = models.CharField(_("address"), blank=True, max_length=300)
    city = models.CharField(_("city"), blank=True, max_length=100)
    nationality = models.CharField(_("nationality"), blank=True, max_length=100)
    annual_income = models.PositiveIntegerField(_("annual income"), default=0)
    image = models.ImageField(
        _("image"), upload_to=guardian_image_path, default="default.png"
    )

    def __str__(self) -> str:
        return f"{self.id}. {self.name}"

    def save(self, *args, **kwargs) -> None:
        """
        Save the instance in the database.
        If image dimensions are too large, shrink it to 300x300.
        """
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)


class Student(models.Model):
    """
    All non-academic information of a student.
    """

    enrollment_id = models.PositiveBigIntegerField(_("enrollment number"), unique=True)
    # class_roll_id = models.PositiveIntegerField(_("class roll number"))
    name = models.CharField(_("name"), max_length=300)
    age = models.PositiveSmallIntegerField(_("age"), default=0)
    gender = models.CharField(
        _("gender"),
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
        max_length=15,
    )
    email = models.EmailField(_("email"), blank=True)
    phone_number = models.CharField(_("phone number"), blank=True, max_length=16)
    address = models.CharField(_("address"), blank=True, max_length=300)
    city = models.CharField(_("city"), blank=True, max_length=100)
    nationality = models.CharField(_("nationality"), blank=True, max_length=100)
    image = models.ImageField(
        _("image"), upload_to=student_image_path, default="default.png"
    )
    # guardians = models.ManyToManyField(Guardian, related_name="wards", blank=True)
    father = models.CharField(_("father"), max_length=300, blank=True)
    mother = models.CharField(_("mother"), max_length=300, blank=True)
    class_section = models.ForeignKey(
        "academics.Class", null=True, default=None, on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return f"{self.enrollment_id} - {self.name}"

    def save(self, *args, **kwargs) -> None:
        """
        Save the instance in the database.
        If image dimensions are too large, shrink it to 300x300.
        """
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)
