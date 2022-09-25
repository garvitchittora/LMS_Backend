from django.conf import settings


def authuser_image_path(instance: settings.AUTH_USER_MODEL, filename: str) -> str:
    """
    Generate the upload path for the image of an authenticable user.
    Authenticable users include admins, teachers and accountants.
    The username of the user is used as the filename for the image.
    """
    extension = filename.split(".")[-1]
    return f"authuser/{instance.username}.{extension}"
