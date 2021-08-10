from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from cryptalme.entities.alert import Alert
from cryptalme.entities.user import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def update_user(self, user_id, **extra_fields):
        """
        update and save a User with the given email
        """
        if not extra_fields.get('email'):
            raise ValueError(_('The Email must be set'))
        user = self.model.objects.get(pk=user_id)
        user.email = extra_fields.get('email')
        user.first_name = extra_fields.get('first_name')
        user.last_name = extra_fields.get('last_name')
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class UserModel(AbstractUser):
    username = None
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    @classmethod
    def from_entity(cls, user: User) -> 'UserModel':
        return UserModel(first_name=user.first_name, last_name=user.last_name, email=user.email, password=user.password)

    def to_entity(self) -> User:
        return User(first_name=self.first_name, last_name=self.last_name, email=self.email)

    @classmethod
    def create_simple_user(cls, user: User) -> 'UserModel':
        user = UserModel.objects.create_user(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            password=user.password,
        )
        return user

    @classmethod
    def update_simple_user(cls, user_id, user: User) -> 'UserModel':
        user = UserModel.objects.update_user(
            id=user_id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            password=user.password,
        )
        return user


class AlertModel(models.Model):
    stop_price = models.IntegerField("Target price")
    alert_type = models.CharField("Alert type", max_length=10)
    triggered = models.BooleanField(default=False)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def from_entity(cls, alert: Alert) -> 'AlertModel':
        return AlertModel(stop_price=alert.stop_price, alert_type=alert.alert_type)

    def to_entity(self) -> Alert:
        return Alert(alert_id=self.id, stop_price=self.stop_price, alert_type=self.alert_type, user=self.user.to_entity())
