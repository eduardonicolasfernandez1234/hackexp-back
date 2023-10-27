from django.db import models

from authentication.models import UserBusiness
from common.models.base_model import BaseModel


class Account(BaseModel):
    name = models.CharField(max_length=255)
    number_account = models.CharField(max_length=20)
    index = models.PositiveIntegerField()

    # FK
    business = models.ForeignKey(
        UserBusiness, on_delete=models.PROTECT, related_name='account_business')
