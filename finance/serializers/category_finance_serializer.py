from rest_framework import serializers

from finance.models import CategoryFinance


class CategoryFinanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryFinance
        fields = '__all__'
