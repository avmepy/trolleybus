from django.contrib.auth.models import User
from django.db import models


class Stop(models.Model):

    name = models.CharField(verbose_name="Назва зупинки", max_length=50)
    address = models.CharField(verbose_name="Адреса", max_length=50, blank=True)

    def __str__(self):
        return f"зуп. {self.name}"


class ScheduledStop(models.Model):

    stop = models.ForeignKey(Stop, on_delete=models.DO_NOTHING)
    time = models.TimeField(verbose_name="Час зупинки")

    def __str__(self):
        return f"Scheduled stop {self.stop} {self.time}"


class Route(models.Model):

    name = models.CharField(verbose_name="Назва маршруту", max_length=50, blank=True)
    stops = models.ManyToManyField(Stop)

    def __str__(self):
        return f"Route {self.name}"


class Schedule(models.Model):

    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    cruise_number = models.IntegerField(verbose_name="Номер рейсу")
    start_time = models.TimeField(verbose_name="Початок рейсу", blank=True)
    end_time = models.TimeField(verbose_name="Кінець рейсу", blank=True)
    scheduled_stops = models.ManyToManyField(ScheduledStop)

    def __str__(self):
        return f"Schedule #{self.cruise_number} route {self.route}"


class ShiftKinds(models.Model):

    number = models.IntegerField(verbose_name="Номер зміни")
    start_time = models.TimeField(verbose_name="Початок зміни")
    end_time = models.TimeField(verbose_name="Кінець зміни")

    def __str__(self):
        return f"Kind shift {self.number} from {self.start_time} till {self.end_time}"


class Shift(models.Model):

    driver = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shift_kind = models.ForeignKey(ShiftKinds, on_delete=models.DO_NOTHING)
    date = models.DateField(verbose_name="Дата")
    schedules = models.ManyToManyField(Schedule)

    def __str__(self):
        return f"Shift {self.shift_kind} {self.driver}"
