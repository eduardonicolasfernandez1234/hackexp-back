from rest_framework import serializers

from authentication.models import UserBusiness
from authentication.serializers import UserRegisterSerializer


class UserBusinessRegisterSerializer(UserRegisterSerializer):
    full_name = serializers.CharField(required=False)
    phone = serializers.CharField(max_length=30, required=False)
    gender = serializers.IntegerField(min_value=0, max_value=2, required=False)

    class Meta:
        model = UserBusiness
        fields = ('first_name', 'last_name', 'email', 'password',
                  'password_confirmation', 'phone', 'gender')


class UserBusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserBusiness
        fields = '__all__'
