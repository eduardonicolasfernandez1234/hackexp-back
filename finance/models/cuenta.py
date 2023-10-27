from django.db import models

from common.models.base_model import BaseModel


class Cuenta(BaseModel):
    name = models.CharField(max_length=255)
    number_account = models.CharField(max_length=20)
    index = models.PositiveIntegerField()
