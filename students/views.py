from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from students.models import Guardian
from students.serializers import GuardianSerializer
from users.permissions import IsAdmin, IsTeacher


class GuardianListCreateView(ListCreateAPIView):
    """
    GET: List all guardians
    POST: Create a new Guardian
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = GuardianSerializer
    queryset = Guardian.objects.all()


class GuardianReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    GET: Read a single guardian instance
    PUT/PATCH: Update guardian information
    DELETE: Delete guardian instance
    """

    permission_classes = [IsAuthenticated, IsAdmin | IsTeacher]
    serializer_class = GuardianSerializer
    queryset = Guardian.objects.all()
