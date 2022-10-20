from django.db import models


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
