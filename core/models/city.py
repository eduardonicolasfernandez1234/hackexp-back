from django.db import models

from common.models.base_model import BaseModel
from core.models import Country


class City(BaseModel):
    name = models.CharField(max_length=255)

    # FK
    country = models.ForeignKey(
        Country, on_delete=models.RESTRICT, related_name='city_country')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
