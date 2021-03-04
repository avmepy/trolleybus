from django.db import models


class State(models.Model):
    id = models.IntegerField(
        primary_key=True)
    name = models.TextField(
        blank=True, null=True)


class Trolleybus(models.Model):
    id = models.IntegerField(
        primary_key=True)
    created_date = models.DateField(
        blank=True, null=True)
    last_maintenance_date = models.DateField(
        blank=True, null=True)
    state = models.ForeignKey(
        'State',
        on_delete=models.DO_NOTHING,
        blank=True, null=True)


class StopPoint(models.Model):
    id = models.IntegerField(
        primary_key=True)
    name = models.TextField(
        blank=True, null=True)


class Schedule(models.Model):
    id = models.IntegerField(
        primary_key=True)
    route = models.ForeignKey(
        'Route',
        on_delete=models.DO_NOTHING)
    date = models.TimeField(
        blank=True, null=True)
    stop_point = models.ForeignKey(
        'StopPoint',
        on_delete=models.DO_NOTHING)


class Route(models.Model):
    id = models.IntegerField(
        primary_key=True)
    stop_points = models.ManyToManyField(
        'StopPoint')
    schedule = models.ForeignKey(
        'Schedule',
        on_delete=models.DO_NOTHING)
