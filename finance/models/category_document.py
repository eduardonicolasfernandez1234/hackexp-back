from django.db import models

from authentication.models import UserBusiness
from common.models.base_model import BaseModel


class CategoryDocument(BaseModel):
    name = models.CharField(max_length=255)

    # FK
    business = models.ForeignKey(
        UserBusiness, on_delete=models.PROTECT, related_name='category_document_business')
