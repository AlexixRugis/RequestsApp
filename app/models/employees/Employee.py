from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.core.validators import RegexValidator
from django.utils import timezone

from .Post import *
from .EmployeeManager import *


class Employee(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)

    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    date_joined = models.DateField(default=timezone.now)

    USERNAME_FIELD = 'phone_number'

    name = models.CharField(max_length=200)
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)

    objects = EmployeeManager()

    def __str__(self):
        return self.name