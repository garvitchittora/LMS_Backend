from django.contrib.auth import authenticate, get_user_model
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.views import APIView

from users.filters import SEARCH_FIELDS, UserFilter
from users.permissions import IsAdmin
from users.serializers import LoginSerializer, UserSerializer
from users.utils import get_tokens_for_user

User = get_user_model()


class TokenObtainPairView(APIView):
    """Authenticate user and return refresh-access token pair on success"""

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get("username")
        password = serializer.data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            msg = {"error": "invalid credentials"}
            return Response(msg, HTTP_401_UNAUTHORIZED)
        response = {
            "success": "User Authenticated",
            "is_admin": user.is_admin,
            "is_teacher": user.is_teacher,
            "is_accountant": user.is_accountant,
        }
        response.update(get_tokens_for_user(user))
        return Response(response, HTTP_200_OK)


class UserCreateView(CreateAPIView):
    """Concrete view to create a new User instance"""

    permission_classes = [IsAuthenticated, IsAdmin | IsAdminUser]
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
