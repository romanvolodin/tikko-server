from rest_framework import viewsets
from rest_framework import permissions
from .models import (
    Project,
)
from .serializers import (
    ProjectSerializer,
)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]