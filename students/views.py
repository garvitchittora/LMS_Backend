from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from students.filters import GuardianFilter, StudentFilter
from students.models import Guardian, Student
from students.serializers import GuardianSerializer, StudentSerializer
from users.permissions import IsAdmin, IsTeacher


class GuardianListCreateView(ListCreateAPIView):
    """
    GET: List all guardians
    POST: Create a new Guardian
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = GuardianSerializer
    queryset = Guardian.objects.all()
    filterset_class = GuardianFilter


class GuardianReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single guardian instance
    PUT/PATCH: Update guardian information
    DELETE: Delete guardian instance
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = GuardianSerializer
    queryset = Guardian.objects.all()


class StudentListCreateView(ListCreateAPIView):
    """
    GET: List all students
    POST: Create a new student
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    filterset_class = StudentFilter


class StudentReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single student instance
    PUT/PATCH: Update student information
    DELETE: Delete student instance
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
