from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image
from users.utils import GenderChoices

from students.utils import guardian_image_path


class Guardian(models.Model):
    """
    Stores information of the guardian/parent of a student.
    """
    name = models.CharField(_("name"), max_length=300, blank=True)
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
