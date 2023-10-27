from django.db.models import DecimalField, F, Sum
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from finance.models import Transaction
from finance.serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=False, methods=['post'], url_path='estado-resultado', name='obtener reporte estado de resultados')
    def obtener_estado_resultado(self, request, pk=None, *args, **kwargs):
        ingresos_totales = Transaction.objects.filter(credit_account__name='Ventas').aggregate(
            total_ingresos=Sum(F('amount'), output_field=DecimalField()))

        gastos_totales = Transaction.objects.filter(debit_account__name='Caja').aggregate(
            total_gastos=Sum(F('amount'), output_field=DecimalField()))

        total_ingresos = ingresos_totales['total_ingresos'] or 0
        total_gastos = gastos_totales['total_gastos'] or 0

        ganancia_neta = total_ingresos - total_gastos

        estado_resultados_data = {
            "ingresos_totales": total_ingresos,
            "gastos_totales": total_gastos,
            "ganancia_neta": ganancia_neta
        }

        return JsonResponse(estado_resultados_data)
