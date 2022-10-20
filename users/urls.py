from django.urls import path

from users import views

urlpatterns = [
    path("add", views.UserCreateView.as_view()),
    path("list", views.UserListView.as_view()),
    path("<int:pk>", views.UserRetrieveUpdateDestroyView.as_view()),
]
