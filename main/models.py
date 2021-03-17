from django.db import models


class TrolleybusState(models.Model):
    id = models.AutoField(
        primary_key=True)
    name = models.TextField(
        blank=True, null=True)

    def __str__(self):
        return self.name


class Trolleybus(models.Model):
    id = models.AutoField(
        primary_key=True)
    car_number = models.CharField(
        max_length=50,
        default=None,
        unique=True)
    created_date = models.DateField(
        blank=True, null=True)
    last_maintenance_date = models.DateField(
        blank=True, null=True)
    state = models.ForeignKey(
        'TrolleybusState',
        on_delete=models.DO_NOTHING,
        blank=True, null=True)
    route = models.ForeignKey(
        'Route',
        default=None,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Тролейбус №{self.id}'


class StopPoint(models.Model):
    id = models.AutoField(
        primary_key=True)
    name = models.TextField(
        blank=True, null=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    id = models.AutoField(
        primary_key=True)
    time = models.TimeField(
        blank=True, null=True)
    stop_point = models.ForeignKey(
        'StopPoint',
        on_delete=models.DO_NOTHING)
    route = models.ForeignKey(
        'Route',
        default=None,
        on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Route: {self.route.name}, StopPoint: {self.stop_point.name}, Time:{self.time}'


class Route(models.Model):
    id = models.AutoField(
        primary_key=True)
    name = models.TextField(
        blank=True, null=True)

    def __str__(self):
        return self.name
