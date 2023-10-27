from django.core.validators import MinValueValidator
from django.db import models

from authentication.models import UserBusiness
from common.models.base_model import BaseModel
from finance.models import Account, CategoryFinance


class Income(BaseModel):

    descripción = models.TextField()
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    # FK
    business = models.ForeignKey(
        UserBusiness, on_delete=models.SET_NULL, null=True, related_name='income_business')
    account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, related_name='income_account', null=True)
    category_finance = models.ForeignKey(
        CategoryFinance, on_delete=models.PROTECT, related_name='income_category_finance')
