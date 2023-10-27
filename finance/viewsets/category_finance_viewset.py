from rest_framework import viewsets

from finance.models import CategoryFinance
from finance.serializers import CategoryFinanceSerializer


class CategoryFinanceViewSet(viewsets.ModelViewSet):
    queryset = CategoryFinance.objects.all()
    serializer_class = CategoryFinanceSerializer
