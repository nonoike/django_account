from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        return self._save_user(email, password, False)

    def create_superuser(self, email, password):
        return self._save_user(email, password, True)

    def _save_user(self, email, password, is_admin):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), is_admin=is_admin)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    user_name = models.CharField(max_length=255, null=True, default=None)
    password = models.CharField(max_length=255)
    is_email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    cancelled_at = models.DateTimeField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def last_login(self):
        raise NotImplementedError

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_active(self):
        return not self.cancelled_at

    class Meta:
        db_table = 'users'
