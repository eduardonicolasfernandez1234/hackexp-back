from rest_framework import viewsets

from finance.models import CategoryDocument
from finance.serializers import CategoryDocumentSerializer


class CategoryDocumentViewSet(viewsets.ModelViewSet):
    queryset = CategoryDocument.objects.all()
    serializer_class = CategoryDocumentSerializer
