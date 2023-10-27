from rest_framework import serializers

from authentication.models import UserAdmin
from authentication.serializers import UserRegisterSerializer


class UserAdminRegisterSerializer(UserRegisterSerializer):
    full_name = serializers.CharField(required=False)
    phone = serializers.CharField(max_length=30, required=False)
    gender = serializers.IntegerField(min_value=0, max_value=2, required=False)

    class Meta:
        model = UserAdmin
        fields = ('first_name', 'last_name', 'email', 'password',
                  'password_confirmation', 'phone', 'gender')


class UserAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAdmin
        fields = '__all__'
