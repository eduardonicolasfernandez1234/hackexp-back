from rest_framework import serializers

from core.models import Area


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'
