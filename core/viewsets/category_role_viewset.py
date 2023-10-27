from rest_framework import viewsets

from core.models import CategoryRole
from core.serializers import CategoryRoleSerializer


class CategoryRoleViewSet(viewsets.ModelViewSet):
    queryset = CategoryRole.objects.all()
    serializer_class = CategoryRoleSerializer
