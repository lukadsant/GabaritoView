from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError

#
# class Country(models.Model):
#     title = models.CharField(max_length=255)
#     code = models.CharField(max_length=25)
#
#     class Meta:
#         verbose_name = _('Country')
#         verbose_name_plural = _('Countries')
#         ordering = ['title']
#
#     def __str__(self):
#         return self.title
#


class User(AbstractUser):

    objects = UserManager()

    username = models.CharField(max_length=25, blank=True, null=True, default='Dynamic insert')
    name = models.CharField(_('Name of user'), max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
