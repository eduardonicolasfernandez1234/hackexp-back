from django.db import models

from authentication.models import UserBusiness
from common.models.base_model import BaseModel
from datetime import date


class JournalEntry(BaseModel):
    """
    Representa un asiento contable que puede incluir varios detalles de documentos.
    """

    date = models.DateField(default=date.today)
    description = models.CharField(max_length=255)

    # FK
    business = models.ForeignKey(
        UserBusiness, on_delete=models.SET_NULL, null=True, related_name='journal_entry_business')
