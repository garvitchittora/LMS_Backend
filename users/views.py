from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView

from users.filters import SEARCH_FIELDS, UserFilter
from users.serializers import UserSerializer

User = get_user_model()


class UserCreateView(CreateAPIView):
    """Concrete view to create a new User instance"""

    serializer_class = UserSerializer


class UserListView(ListAPIView):
    """List authenticable users"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    filterset_class = UserFilter
    search_fields = SEARCH_FIELDS
