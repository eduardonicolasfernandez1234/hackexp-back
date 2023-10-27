from django.db import models

from common.models.base_model import BaseModel


class CategoryRole(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
