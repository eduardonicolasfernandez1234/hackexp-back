from django.db import models

from common.models.base_model import BaseModel


class Area(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name
