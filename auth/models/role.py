from django.db import models

from common.models.base_model import BaseModel
from core.models import CategoryRole


class Role(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    # FK
    category = models.ForeignKey(
        CategoryRole, on_delete=models.RESTRICT, related_name='role_category')

    def __str__(self) -> str:
        return self.name
