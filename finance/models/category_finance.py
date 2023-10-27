from django.db import models

from auth.models import UserBusiness
from common.models.base_model import BaseModel


class CategoryFinance(BaseModel):
    name = models.CharField(max_length=255)

    # FK
    business = models.ForeignKey(
        UserBusiness, on_delete=models.PROTECT, related_name='category_business')
