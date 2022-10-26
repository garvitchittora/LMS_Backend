from django.urls import path

from academics import views

urlpatterns = [
    path("class", views.ClassListCreateView.as_view()),
    path("class/<int:pk>", views.ClassReadUpdateDeleteView.as_view()),
    path("session", views.AcadSessionCreateListView.as_view()),
    path("session/<int:pk>", views.AcadSessionReadUpdateDeleteView.as_view()),
    path("exam", views.ExamCreateListView.as_view()),
    path("exam/<int:pk>", views.ExamReadUpdateDeleteView.as_view()),
    path("score", views.ScoreCreateListView.as_view()),
    path("score/<int:pk>", views.ScoreReadUpdateDeleteView.as_view()),
    path("subject", views.SubjectCreateListView.as_view()),
    path("subject/<int:pk>", views.SubjectReadUpdateDeleteView.as_view()),
]
