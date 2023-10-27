from django.utils.translation import gettext as _
from rest_framework import serializers

from auth.models import User
from common.utils.validations.regex_validations import RegexValidations


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name',
                  'user_type', 'full_name']


class UserRegisterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=300)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, max_length=12, style={
                                     'input_type': 'password'})
    password_confirmation = serializers.CharField(
        min_length=6, max_length=12, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['full_name', 'first_name', 'last_name',
                  'email', 'password', 'password_confirmation']

    def val_field_password(value):
        if len(value) < 6 or len(value) > 12:
            raise serializers.ValidationError(
                _("The password must be between 6 and 12 characters long."))

        if not RegexValidations.has_lowercase_character(value):
            raise serializers.ValidationError(
                _("The password must contain at least one lowercase character."))

        if not RegexValidations.has_uppercase_character(value):
            raise serializers.ValidationError(
                _("The password must contain at least one uppercase character."))

        if not RegexValidations.has_special_character(value):
            raise serializers.ValidationError(
                _("The password must contain at least one special character."))

        return value

    def val_passwords_match(data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(_("The passwords do not match."))
        return data

    def validate_password(self, value):
        return self.val_field_password(value)

    def validate(self, data):
        return self.val_passwords_match(data)

    def validate_email(self, value):
        has_duplicate_user = User.objects.filter(email=value)
        if has_duplicate_user:
            raise serializers.ValidationError(_("Email field already exists."))
        return value


class UserUpdateSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=300, required=False)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['full_name', 'first_name', 'last_name']


class ResetUserPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, max_length=12, style={
                                     'input_type': 'password'})
    password_confirmation = serializers.CharField(
        min_length=6, max_length=12, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirmation']

    def val_field_password(value):
        if len(value) < 6 or len(value) > 12:
            raise serializers.ValidationError(
                _("The password must be between 6 and 12 characters long."))

        if not RegexValidations.has_lowercase_character(value):
            raise serializers.ValidationError(
                _("The password must contain at least one lowercase character."))

        if not RegexValidations.has_uppercase_character(value):
            raise serializers.ValidationError(
                _("The password must contain at least one uppercase character."))

        if not RegexValidations.has_special_character(value):
            raise serializers.ValidationError(
                _("The password must contain at least one special character."))

        return value

    def val_passwords_match(data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(_("The passwords do not match."))
        return data

    def validate_password(self, value):
        return self.val_field_password(value)

    def validate(self, data):
        return self.val_passwords_match(data)

    def validate_email(self, value):
        user = User.objects.filter(email=value).first()
        if not user:
            raise serializers.ValidationError(_("The email not exists."))
        return value
