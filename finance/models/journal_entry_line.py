from django.db import models

from common.models.base_model import BaseModel
from finance.models import Account


class JournalEntryLine(BaseModel):
    """
    Registra los movimientos en las cuentas para un asiento, indicando si es un débito o un crédito.
    """
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=1, choices=[
                            ('D', 'Debit'), ('C', 'Credit')])

    # FK
    journal_entry = models.ForeignKey(
        'JournalEntry', on_delete=models.SET_NULL, null=True, related_name='journal_entry_line_journal_entry')
    account = models.ForeignKey(Account, on_delete=models.SET_NULL,
                                null=True, related_name='journal_entry_line_account')
