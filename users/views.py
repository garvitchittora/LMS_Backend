from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.filters import SEARCH_FIELDS, UserFilter
from users.permissions import IsAdmin
from users.serializers import UserSerializer

User = get_user_model()


class UserCreateView(CreateAPIView):
    """Concrete view to create a new User instance"""

    permission_classes = [IsAdmin | IsAdminUser]
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    """List authenticable users"""

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filterset_class = UserFilter
    search_fields = SEARCH_FIELDS


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """Get, update and delete information of an existing user"""

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()
