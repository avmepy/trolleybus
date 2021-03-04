from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """
    extension of the standard User model
    """

    account = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account.first_name} {self.account.last_name}"

    def __repr__(self):
        return f"{self.account.first_name} {self.account.last_name}"

    # TODO
