from rest_framework import serializers

from finance.models import JournalEntry


class JournalEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = JournalEntry
        fields = '__all__'
