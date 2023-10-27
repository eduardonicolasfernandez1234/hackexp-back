from rest_framework import serializers

from finance.models import JournalEntryLine


class JournalEntryLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = JournalEntryLine
        fields = '__all__'
