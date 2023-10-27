from django.core.validators import MinValueValidator
from django.db import models

from common.models.base_model import BaseModel
from finance.models import CategoryFinance


class EntryFinance(BaseModel):

    descripción = models.TextField()
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    # FK
    cuenta = models.ForeignKey('Cuenta', on_delete=models.PROTECT)
    category_finance = models.ForeignKey(
        CategoryFinance, on_delete=models.PROTECT, related_name='entry_category_finance')
