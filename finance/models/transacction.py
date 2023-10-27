from datetime import date

from django.core.validators import MinValueValidator
from django.db import models

from common.models.base_model import BaseModel
from finance.models import Account


class Transaction(BaseModel):
    date = models.DateField(default=date.today)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    debit_account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, related_name='transaction_debit', null=True)
    credit_account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, related_name='transaction_credit', null=True)


"""
* Cuando se aumenta un activo, se registra un débito en la cuenta del activo.
* Cuando se aumenta un pasivo o el capital, se registra un crédito en la cuenta del pasivo o del capital.
* Cuando se registra un ingreso, se registra un crédito en la cuenta de ingresos.
* Cuando se registra un gasto, se registra un débito en la cuenta de gastos.
"""
