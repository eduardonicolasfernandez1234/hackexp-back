from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    USER_TYPE_BUSINESS = 0
    USER_TYPE_EMPLOYEE = 1
    USER_TYPE_ADMIN = 2

    USER_TYPES = (
        (USER_TYPE_BUSINESS, 'Business'),
        (USER_TYPE_EMPLOYEE, 'Employee'),
        (USER_TYPE_ADMIN, 'Admin')
    )

    GENDER_TYPE_MALE = 0
    GENDER_TYPE_FEMALE = 1
    GENDER_TYPE_OTHER = 2
    GENDER_TYPES = (
        (GENDER_TYPE_MALE, 'Male'),
        (GENDER_TYPE_FEMALE, 'Female'),
        (GENDER_TYPE_OTHER, 'Other')
    )

    full_name = models.CharField(max_length=300)
    email = models.EmailField(unique=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_TYPES, default=GENDER_TYPE_OTHER)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES)
    is_deleted = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='Groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='User permissions',
        help_text='Specific permissions for this user.',
    )

    def fields_for_create(self):
        return ['first_name', 'last_name', 'email', 'password_confirmation']

    def fields_for_update(self):
        return ['first_name', 'last_name']

    def __str__(self) -> str:
        return self.full_name
