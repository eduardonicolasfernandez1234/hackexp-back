from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import mixins, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from auth.models import User, UserAdmin
from auth.repository import UserAdminRepository, UserRepository
from auth.serializers import UserAdminRegisterSerializer


class UserAdminRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserAdmin.objects.all()
    serializer_class = UserAdminRegisterSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = UserRepository.create_user(
                    request.data, User.USER_TYPE_ADMIN)
                UserAdminRepository.create_user_admin(user_instance=user)
                return Response(data={'sucess': True}, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response(data=e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data='An error occurred while trying to create a UserAdmin', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
