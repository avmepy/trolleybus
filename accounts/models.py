from django.contrib.auth.models import User
from django.db import models
from transports.models import Transport
from routes.models import Schedule


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transport = models.ForeignKey(Transport, on_delete=models.DO_NOTHING, default=None)
    phone = models.CharField(verbose_name='Телефон', blank=True, max_length=20)
    driver_license = models.CharField(verbose_name='Посвідчення водія', blank=True, max_length=20)
    schedules = models.ManyToManyField(Schedule)

    def __str__(self):
        return f'Profile {self.user.username}'
