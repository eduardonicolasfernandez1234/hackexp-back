from rest_framework import viewsets

from core.models import Industry
from core.serializers import IndustrySerializer


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
