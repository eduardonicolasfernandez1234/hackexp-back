from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncWeek, TruncYear
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from finance.models import Expense
from finance.serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    @action(detail=False, methods=['post'], url_path='gasto-diario', name='obtener reporte gastos diario')
    def obtener_reporte_diario(self, request, pk=None, *args, **kwargs):
        gastos_diarios = Expense.objects.values('created_at').annotate(
            total_gastos=Sum('amount')).order_by('created_at')

        informe = [{"date": gasto['created_at'], "total_gastos": gasto['total_gastos']}
                   for gasto in gastos_diarios]

        return JsonResponse(informe, safe=False)

    @action(detail=False, methods=['post'], url_path='gasto-semana', name='obtener reporte gasto semanal')
    def obtener_reporte_semana(self, request, pk=None, *args, **kwargs):
        gastos_semanales = Expense.objects.annotate(week=TruncWeek('created_at')).values(
            'week').annotate(total_gastos=Sum('amount')).order_by('week')

        informe = [{"week": gasto['week'], "total_gastos": gasto['total_gastos']}
                   for gasto in gastos_semanales]

        return JsonResponse(informe, safe=False)

    @action(detail=False, methods=['post'], url_path='gasto-mes', name='obtener reporte gasto mensual')
    def obtener_reporte_mes(self, request, pk=None, *args, **kwargs):
        gastos_mensuales = Expense.objects.annotate(month=TruncMonth('created_at')).values(
            'month').annotate(total_gastos=Sum('amount')).order_by('month')

        informe = [{"month": gasto['month'], "total_gastos": gasto['total_gastos']}
                   for gasto in gastos_mensuales]

        return JsonResponse(informe, safe=False)

    @action(detail=False, methods=['post'], url_path='gasto-anio', name='obtener reporte gasto anual')
    def obtener_reporte_anual(self, request, pk=None, *args, **kwargs):
        gastos_anuales = Expense.objects.annotate(year=TruncYear('created_at')).values(
            'year').annotate(total_gastos=Sum('amount')).order_by('year')

        informe = [{"year": gasto['year'], "total_gastos": gasto['total_gastos']}
                   for gasto in gastos_anuales]

        return JsonResponse(informe, safe=False)
