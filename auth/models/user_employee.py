from django.contrib.auth import get_user_model
from django.db import models

from auth.models import Role, UserAdmin
from common.models.base_model import BaseModel
from core.models import Area, City, Position


class UserEmployee(BaseModel):
    short_code = models.CharField(max_length=3)
    profile_image = models.ImageField(null=True, default=None)
    phone = models.CharField(max_length=15, null=True, default=None)

    ci = models.CharField(max_length=10, null=True, default=None)
    other_position = models.CharField(max_length=10, null=True, default=None)
    other_area = models.CharField(max_length=10, null=True, default=None)

    # FK
    business = models.ForeignKey(
        UserAdmin, on_delete=models.RESTRICT, related_name='employee_business')
    user = models.ForeignKey(
        get_user_model(), on_delete=models.RESTRICT, related_name='employee_user')
    city = models.ForeignKey(
        City, on_delete=models.RESTRICT, related_name='employee_city', null=True)
    position = models.ForeignKey(
        Position, on_delete=models.RESTRICT, related_name='employee_position', null=True)
    area = models.ForeignKey(
        Area, on_delete=models.RESTRICT, related_name='employee_area', null=True)
    roles = models.ManyToManyField(
        Role, related_name='employee_roles', default=list())

    def __str__(self) -> str:
        return self.user.full_name
