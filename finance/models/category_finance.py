from django.db import models

from authentication.models import UserBusiness
from common.models.base_model import BaseModel
from finance.models import Account

class CategoryFinance(BaseModel):
    name = models.CharField(max_length=255)

    # FK
    business = models.ForeignKey(
        UserBusiness, on_delete=models.PROTECT, related_name='category_finance_business')
    debit_account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, related_name='category_finance_debit', null=True)
    credit_account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, related_name='category_finance_credit', null=True)
