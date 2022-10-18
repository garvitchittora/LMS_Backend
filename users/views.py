from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from users.serializers import UserSerializer

User = get_user_model()


class UserCreateView(CreateAPIView):
    """Concrete view to create a new User instance"""

    serializer_class = UserSerializer
