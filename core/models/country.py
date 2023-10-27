from django.db import models

from common.models.base_model import BaseModel


class Country(BaseModel):
    country_code = models.CharField(max_length=5, unique=True)
    number_code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.country_code} - {self.name}'
