from django.urls import re_path, include
from rest_framework import routers

from authentication.viewsets import UserAdminRegisterViewSet, UserBusinessRegisterViewSet, UserEmployeeRegisterViewSet

router = routers.DefaultRouter()
router.register(r'create-admin', UserAdminRegisterViewSet)
router.register(r'create-business', UserBusinessRegisterViewSet)
router.register(r'create-employee', UserEmployeeRegisterViewSet)


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
