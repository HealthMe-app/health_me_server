from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, sex, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            sex=sex,
            date_of_birth=date_of_birth
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, sex, date_of_birth, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            sex=sex,
            date_of_birth=date_of_birth,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    first_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    sex = models.BooleanField() # 0m, 1f
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

