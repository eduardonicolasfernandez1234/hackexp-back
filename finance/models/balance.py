from datetime import date

from django.db import models

from authentication.models import UserBusiness
from common.models.base_model import BaseModel
from finance.models import Account


class Balance(BaseModel):
    date = models.DateField(default=date.today)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    # FK
    business = models.ForeignKey(
        UserBusiness, on_delete=models.PROTECT, related_name='balance_business')
    account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True, related_name='balance_account')
