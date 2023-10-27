from django.db import models


from common.models.base_model import BaseModel
from finance.models import Account, Document


class DocumentDetail(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # FK
    document = models.ForeignKey(
        Document, on_delete=models.SET_NULL, null=True, related_name='document_detail_document')
    account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True, related_name='document_detail_account')

"""
Detalle para Factura de Venta (FV-2023-001):

Documento: Factura de Venta (FV-2023-001)
Cuenta: Cuentas por Cobrar
Monto: $1,000.00 (representando el monto pendiente de pago por el cliente)
Detalle para Recibo de Pago (RP-2023-001):

Documento: Recibo de Pago (RP-2023-001)
Cuenta: Caja o Banco
Monto: $1,000.00 (representando el monto recibido del cliente)
Detalle para Comprobante de Gasto (CG-2023-001):

Documento: Comprobante de Gasto (CG-2023-001)
Cuenta: Gastos de Oficina
Monto: $250.00 (representando el monto del gasto en suministros de oficina)
"""