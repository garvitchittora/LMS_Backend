from django.urls import path

from users import views

urlpatterns = [
    path("add", views.UserCreateView.as_view()),
]
