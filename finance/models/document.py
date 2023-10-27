from datetime import date

from django.db import models

from authentication.models import UserBusiness
from common.models.base_model import BaseModel
from finance.models import CategoryDocument


class Document(BaseModel):
    """
     Registra documentos contables, como facturas, recibos, etc., junto con los detalles de las cuentas y montos asociado
    """
    date = models.DateField(default=date.today)
    number = models.CharField(max_length=20)
    description = models.CharField(max_length=255)

    # FK
    business = models.ForeignKey(
        UserBusiness, on_delete=models.SET_NULL, null=True, related_name='document_business')
    category_document = models.ForeignKey(
        CategoryDocument, on_delete=models.SET_NULL, null=True, related_name='document_category_document')


"""
Factura de Venta:

Fecha: 2023-10-15
Número: FV-2023-001
Categoría: Ventas
Descripción: Factura de venta para productos entregados a Cliente A.
Recibo de Pago:

Fecha: 2023-10-20
Número: RP-2023-001
Categoría: Ingresos
Descripción: Recibo de pago recibido de Cliente B para la factura FV-2023-001.
Comprobante de Gasto:

Fecha: 2023-10-25
Número: CG-2023-001
Categoría: Gastos Generales
Descripción: Comprobante de gasto por la compra de suministros de oficina.
"""
