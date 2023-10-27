from rest_framework import serializers

from finance.models import CategoryDocument


class CategoryDocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryDocument
        fields = '__all__'
