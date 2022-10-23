from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin

from academics.models import Class
from academics.serializers import ClassSerializer


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
