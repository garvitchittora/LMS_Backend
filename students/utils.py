import string

from django.db import models
from django.utils.crypto import get_random_string


def guardian_image_path(instance, filename: str) -> str:
    """
    Generate the upload path for the image of a guardian.
    A random string is generated for the image file name.
    """
    extension = filename.split(".")[-1]
    random_name = get_random_string(10, string.ascii_letters + string.digits)
    return f"guardian/{random_name}.{extension}"


def student_image_path(instance, filename: str) -> str:
    """
    Generate the upload path for the image of a student.
    The enrollment number of the student is used as the name of the image file.
    """
    extension = filename.split(".")[-1]
    return f"student/{instance.enrollment_id}.{extension}"


class GuardianStudentRelations(models.TextChoices):
    """
    Provides choices for the relationship of a student with a guardian.
    The guardian can be the student's father, mother, or any other relative.
    """

    FATHER = "FATHER", "Father"
    MOTHER = "MOTHER", "Mother"
    RELATIVE = "RELATIVE", "Relative"
    NON_RELATED = "NON RELATED", "Non Related"
