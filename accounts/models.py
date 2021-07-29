from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    phone = models.CharField(max_length=20,
                             verbose_name='Телефон',
                             blank=True,
                             null=True
                             )
    avatar = models.ImageField(verbose_name='Аватар',
                               blank=True,
                               null=True)

    def save(self, *args, **kwargs):
        return super(AdvUser, self).save(*args, **kwargs)
