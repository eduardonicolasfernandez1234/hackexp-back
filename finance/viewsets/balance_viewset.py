from rest_framework import viewsets

from finance.models import Balance
from finance.serializers import BalanceSerializer


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
