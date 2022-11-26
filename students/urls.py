from django.urls import path

from students import views

urlpatterns = [
    path("guardians", views.GuardianListCreateView.as_view()),
    path("guardians/<int:pk>", views.GuardianReadUpdateDeleteView.as_view()),
    path("students", views.StudentListCreateView.as_view()),
    path("students/<int:pk>", views.StudentReadUpdateDeleteView.as_view()),
]
