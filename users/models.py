from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    A core class defining the usable User model derived from AbstractUser.
    It is referred by the `settings.AUTH_USER_MODEL` attribute of the project.
    """
    is_admin = models.BooleanField(_("admin"), default=False)
    is_teacher = models.BooleanField(_("teacher"), default=False)
    is_accountant = models.BooleanField(_("accountant"), default=False)
