from django.db import models


class Stop(models.Model):

    name = models.CharField(verbose_name="Назва зупинки", max_length=50)
    address = models.CharField(verbose_name="Адреса", max_length=50, blank=True)

    def __str__(self):
        return f"Stop {self.name}"


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
    scheduled_stops = models.ManyToManyField(ScheduledStop)

    def __str__(self):
        return f"Schedule #{self.cruise_number} route {self.route}"
