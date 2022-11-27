from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    """Get refresh-access token pair for the given user instance"""
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def authuser_image_path(instance, filename: str) -> str:
    """
    Generate the upload path for the image of an authenticable user.
    Authenticable users include admins, teachers and accountants.
    The username of the user is used as the filename for the image.
    """
    extension = filename.split(".")[-1]
    return f"authuser/{instance.username}.{extension}"


class GenderChoices(models.TextChoices):
    """
    Contains the available choices for the `gender` field.
    """

    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"
    OTHER = "OTHER", "Other"
