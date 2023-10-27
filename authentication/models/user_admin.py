from django.contrib.auth import get_user_model
from django.db import models

from common.models.base_model import BaseModel
from core.models import City


class UserAdmin(BaseModel):
    short_code = models.CharField(max_length=3)
    profile_image = models.ImageField(null=True, default=None)
    phone = models.CharField(max_length=15, null=True, default=None)
    web_site = models.URLField(null=True, default=None)

    # FK
    user = models.ForeignKey(
        'User', on_delete=models.RESTRICT, related_name='admin_user')
    city = models.ForeignKey(
        City, on_delete=models.RESTRICT, related_name='admin_city', null=True)

    def __str__(self) -> str:
        return self.user.full_name
