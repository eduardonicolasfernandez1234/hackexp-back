from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncWeek, TruncYear
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from finance.models import Income
from finance.serializers import IncomeSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    @action(detail=False, methods=['post'], url_path='ingreso-diario', name='obtener reporte ingreso diario')
    def obtener_reporte_diario(self, request, pk=None, *args, **kwargs):
        gastos_diarios = Income.objects.values('created_at').annotate(
            total_ingresos=Sum('amount')).order_by('created_at')

        informe = [{"date": gasto['created_at'], "total_ingresos": gasto['total_ingresos']}
                for gasto in gastos_diarios]

        return JsonResponse(informe, safe=False)

    @action(detail=False, methods=['post'], url_path='ingreso-semana', name='obtener reporte ingreso semanal')
    def obtener_reporte_semana(self, request, pk=None, *args, **kwargs):
        ingresos_semanales = Income.objects.annotate(week=TruncWeek('created_at')).values(
            'week').annotate(total_ingresos=Sum('amount')).order_by('week')

        informe = [{"week": ingreso['week'], "total_ingresos": ingreso['total_ingresos']}
                   for ingreso in ingresos_semanales]

        return JsonResponse(informe, safe=False)

    @action(detail=False, methods=['post'], url_path='ingreso-mes', name='obtener reporte ingreso mensual')
    def obtener_reporte_mes(self, request, pk=None, *args, **kwargs):
        ingresos_mensuales = Income.objects.annotate(month=TruncMonth('created_at')).values(
            'month').annotate(total_ingresos=Sum('amount')).order_by('month')

        informe = [{"month": ingreso['month'], "total_ingresos": ingreso['total_ingresos']}
                   for ingreso in ingresos_mensuales]

        return JsonResponse(informe, safe=False)

    @action(detail=False, methods=['post'], url_path='ingreso-anio', name='obtener reporte anual')
    def obtener_reporte_anual(self, request, pk=None, *args, **kwargs):
        ingresos_anuales = Income.objects.annotate(year=TruncYear('created_at')).values(
            'year').annotate(total_ingresos=Sum('amount')).order_by('year')

        informe = [{"year": ingreso['year'], "total_ingresos": ingreso['total_ingresos']}
                   for ingreso in ingresos_anuales]

        return JsonResponse(informe, safe=False)
