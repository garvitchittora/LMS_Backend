from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin, IsTeacher

from academics.filters import ExamFilter, ScoreFilter, SubjectFilter
from academics.models import AcademicSession, Class, Examination, Score, Subject
from academics.serializers import (
    AcademicSessionSerializer,
    ClassSerializer,
    ExamSerializer,
    ScoreSerializer,
    SubjectSerializer,
)


class ClassListCreateView(ListCreateAPIView):
    """
    GET: List all classes.
    POST: Create a new class.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ClassSerializer
    queryset = Class.objects.all()

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method != "GET":
            permissions.append(IsAdmin())
        return permissions


class ClassReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single class instance.
    PUT/PATCH: Update class information.
    DELETE: Delete class instance.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ClassSerializer
    queryset = Class.objects.all()

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method != "GET":
            permissions.append(IsAdmin())
        return permissions


class AcadSessionCreateListView(ListCreateAPIView):
    """
    GET: List all academic sessions
    POST: Create a new session.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = AcademicSessionSerializer
    queryset = AcademicSession.objects.all()

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method != "GET":
            permissions.append(IsAdmin())
        return permissions


class AcadSessionReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single session instance.
    PUT/PATCH: Update session information.
    DELETE: Delete session instance.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = AcademicSessionSerializer
    queryset = AcademicSession.objects.all()

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method != "GET":
            permissions.append(IsAdmin())
        return permissions


class ExamCreateListView(ListCreateAPIView):
    """
    GET: List all exams.
    POST: Create a new exam.
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = ExamSerializer
    queryset = Examination.objects.all()
    filterset_class = ExamFilter


class ExamReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single examination instance.
    PUT/PATCH: Update exam information.
    DELETE: Delete exam instance.
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = ExamSerializer
    queryset = Examination.objects.all()


class ScoreCreateListView(ListCreateAPIView):
    """
    GET: List all scores.
    POST: Add a new score.
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
    filterset_class = ScoreFilter


class ScoreReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single score instance.
    PUT/PATCH: Update score information.
    DELETE: Delete score instance.
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()


class SubjectCreateListView(ListCreateAPIView):
    """
    GET: List all subjects.
    POST: Add a new subject.
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    filterset_class = SubjectFilter


class SubjectReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single subject instance.
    PUT/PATCH: Update subject information.
    DELETE: Delete subject instance.
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
