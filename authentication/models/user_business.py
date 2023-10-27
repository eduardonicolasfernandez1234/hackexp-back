from django.db import models

from common.models.base_model import BaseModel
from core.models import City, Industry


class UserBusiness(BaseModel):

    short_code = models.CharField(max_length=3)
    profile_image = models.ImageField(null=True, default=None)
    phone = models.CharField(max_length=15, null=True, default=None)
    web_site = models.URLField(null=True, default=None)

    name_business = models.CharField(max_length=40, null=True, default=None)
    nit = models.CharField(max_length=12, null=True, default=None)
    address = models.CharField(max_length=120, null=True, default=None)
    telephone = models.CharField(max_length=15, null=True, default=None)
    other_industry = models.CharField(max_length=120, null=True, default=None)
    total_employeers = models.PositiveIntegerField(default=0)

    # FK
    user = models.ForeignKey(
        'User', on_delete=models.RESTRICT, related_name='business_user')
    city = models.ForeignKey(
        City, on_delete=models.RESTRICT, related_name='business_city', null=True)
    industry = models.ForeignKey(
        Industry, on_delete=models.RESTRICT, related_name='business_industry', null=True)

    def __str__(self) -> str:
        return self.user.full_name
