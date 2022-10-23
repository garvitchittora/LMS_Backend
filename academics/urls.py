from django.urls import path

from academics import views

urlpatterns = [
    path("class", views.ClassListCreateView.as_view()),
    path("class/<int:pk>", views.ClassReadUpdateDeleteView.as_view()),
]
