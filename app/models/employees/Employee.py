from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils import timezone

from .Post import *
from .EmployeeManager import *


class Employee(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number']

    name = models.CharField(max_length=200)
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin