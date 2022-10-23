from django.urls import path

from academics import views

urlpatterns = [
    path("class", views.ClassListCreateView.as_view()),
    path("class/<int:pk>", views.ClassReadUpdateDeleteView.as_view()),
    path("session/add", views.AcadSessionCreateView.as_view()),
    path("session/list", views.AcadSessionListView.as_view()),
    path("session/<int:pk>", views.AcadSessionReadUpdateDeleteView.as_view()),
]
