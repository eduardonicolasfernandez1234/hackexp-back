from rest_framework import serializers

from core.models import CategoryRole


class CategoryRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryRole
        fields = '__all__'
