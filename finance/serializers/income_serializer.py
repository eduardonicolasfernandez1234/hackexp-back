from rest_framework import serializers

from finance.models import Income


class IncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Income
        fields = '__all__'
