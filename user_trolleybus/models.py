from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserTrolleybus(models.Model):
    """ extension user model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name="Телефон", max_length=20)
    birth_date = models.DateField(verbose_name="Дата народження")
    experience = models.IntegerField(verbose_name="Стаж")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserTrolleybus.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
