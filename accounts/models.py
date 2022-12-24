from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Third party apps
from phonenumber_field.modelfields import PhoneNumberField
# Local apps
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    phone = PhoneNumberField(unique=True, region='IR')
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
