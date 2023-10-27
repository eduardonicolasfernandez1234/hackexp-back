from rest_framework import viewsets

from finance.models import JournalEntry
from finance.serializers import JournalEntrySerializer


class JournalEntryViewSet(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
