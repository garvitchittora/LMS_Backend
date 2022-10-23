from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin

from academics.models import AcademicSession, Class
from academics.serializers import AcademicSessionSerializer, ClassSerializer


class ClassListCreateView(ListCreateAPIView):
    """
    GET: List all classes.
    POST: Create a new class.
    """

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = ClassSerializer
    queryset = Class.objects.all()


class ClassReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single class instance.
    PUT/PATCH: Update class information.
    DELETE: Delete class instance.
    """

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = ClassSerializer
    queryset = Class.objects.all()


class AcadSessionCreateView(CreateAPIView):
    """
    POST: Create a new session.
    """

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AcademicSessionSerializer
    queryset = AcademicSession.objects.all()


class AcadSessionListView(ListAPIView):
    """
    GET: List all academic sessions
    """

    permission_classes = [IsAuthenticated]
    serializer_class = AcademicSessionSerializer
    queryset = AcademicSession.objects.all()


class AcadSessionReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single session instance.
    PUT/PATCH: Update session information.
    DELETE: Delete session instance.
    """

    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = AcademicSessionSerializer
    queryset = AcademicSession.objects.all()
