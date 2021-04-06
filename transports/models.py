from django.db import models


class Condition(models.Model):

    title = models.CharField(verbose_name="Короткий опис", max_length=20)
    description = models.TextField(verbose_name="Детальний опис", blank=True)

    def __str__(self):
        return f"Condition {self.title}"


class Transport(models.Model):

    reg_plate = models.CharField(verbose_name="Автомобільний номер", max_length=10)
    condition = models.CharField(verbose_name="Стан", max_length=1000, blank=True, default="ok")
    mileage = models.IntegerField(verbose_name="Пробіг (тис. км)", blank=True)

    def __str__(self):
        return f"Transport {self.reg_plate}"
