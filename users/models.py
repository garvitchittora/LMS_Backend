from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from users.utils import GenderChoices, authuser_image_path


class User(AbstractUser):
    """
    A core class defining the usable User model derived from AbstractUser.
    It is referred by the `settings.AUTH_USER_MODEL` attribute of the project.
    """

    # Remove first_name and last_name
    first_name = None
    last_name = None

    # User types
    is_admin = models.BooleanField(_("admin"), default=False)
    is_teacher = models.BooleanField(_("teacher"), default=False)
    is_accountant = models.BooleanField(_("accountant"), default=False)

    # General details
    name = models.CharField(_("name"), blank=True, max_length=50)
    gender = models.CharField(
        _("gender"),
        choices=GenderChoices.choices,
        default=GenderChoices.MALE,
        max_length=15,
    )
    phone_number = models.CharField(_("phone number"), blank=True, max_length=16)
    address = models.CharField(_("address"), blank=True, max_length=300)
    city = models.CharField(_("city"), blank=True, max_length=100)
    nationality = models.CharField(_("nationality"), blank=True, max_length=100)
    social_category = models.CharField(_("social category"), blank=True, max_length=100)
    designation = models.CharField(_("designation"), blank=True, max_length=100)
    annual_income = models.PositiveIntegerField(_("annual income"), default=0)
    image = models.ImageField(
        _("image"), upload_to=authuser_image_path, default="default.png"
    )

    def save(self, *args, **kwargs) -> None:
        """
        Save the User instance in the database.
        If image dimensions are too large, shrink it to 300x300.
        """
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.image.path)
