from rest_framework import viewsets

from finance.models import DocumentDetail
from finance.serializers import DocumentDetailSerializer


class DocumentDetailViewSet(viewsets.ModelViewSet):
    queryset = DocumentDetail.objects.all()
    serializer_class = DocumentDetailSerializer
