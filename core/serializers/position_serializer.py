from rest_framework import serializers

from core.models import Position


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'
