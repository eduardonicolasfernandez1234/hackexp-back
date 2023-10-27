from rest_framework import viewsets

from finance.models import JournalEntryLine
from finance.serializers import JournalEntryLineSerializer


class JournalEntryLineViewSet(viewsets.ModelViewSet):
    queryset = JournalEntryLine.objects.all()
    serializer_class = JournalEntryLineSerializer
