import string

from django.utils.crypto import get_random_string


def guardian_image_path(instance, filename: str) -> str:
    """
    Generate the upload path for the image of a guardian.
    The `id` (primary key) of the guardian model is used 
    as the name of the image file.
    """
    extension = filename.split(".")[-1]
    random_name = get_random_string(10, string.ascii_letters + string.digits)
    return f"student/{random_name}.{extension}"
