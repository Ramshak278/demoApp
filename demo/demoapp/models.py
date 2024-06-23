from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.
from django.utils import timezone


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email=self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self,email,password=None,**extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email,password,**extra_fields)
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("username", email)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    Id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    creation_time = models.DateTimeField(default=timezone.now)
    deletion_time = models.DateTimeField(default=timezone.now)
    isDeleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    firstName = models.CharField(max_length=30,null=True,blank=True)
    lastName = models.CharField(max_length=30,null=True,blank=True)
    objects= UserManager()
    USERNAME_FIELD = 'email'
