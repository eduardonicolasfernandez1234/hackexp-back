from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import mixins, serializers, status, viewsets
from rest_framework.response import Response

from authentication.models import User, UserEmployee
from authentication.repository import UserEmployeeRepository, UserRepository
from authentication.serializers import UserEmployeeRegisterSerializer


class UserEmployeeRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserEmployee.objects.all()
    serializer_class = UserEmployeeRegisterSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = UserRepository.create_user(
                    request.data, User.USER_TYPE_EMPLOYEE)
                UserEmployeeRepository.create_user_employee(user_instance=user, business_id=request.data['business_id'])
                return Response(data={'sucess': True}, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response(data=e.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data='An error occurred while trying to create a UserEmployee' + str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
