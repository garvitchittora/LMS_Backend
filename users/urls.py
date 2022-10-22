from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

urlpatterns = [
    path("add", views.UserCreateView.as_view()),
    path("list", views.UserListView.as_view()),
    path("<int:pk>", views.UserRetrieveUpdateDestroyView.as_view()),
    path("token", TokenObtainPairView.as_view()),
    path("token/refresh", TokenRefreshView.as_view()),
]
