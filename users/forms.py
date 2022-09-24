from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from users.models import User


class UserCreationForm(BaseUserCreationForm):
    """
    Form used for User model. It changes the model reference
    of the original `UserCreationForm` to the custom User model.
    """
    class Meta:
        model = User
        fields = "__all__"
