from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="core_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="core_user_set")
    username = models.CharField(max_length=60, blank=True, null=True,default="def")
    email = models.EmailField(_("email address"), unique=True )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
