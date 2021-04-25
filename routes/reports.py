#!/usr/bin/env python3
# -*-encoding: utf-8-*-

from routes.models import Shift, Schedule


def worked_hours(driver, date_from, date_to):
    shifts = Shift.objects.filter(driver=driver, date__range=[date_from, date_to])
    schedules = []
    for shift in shifts:
        schedules += [Schedule.objects.filter(shift=shift)]
    return shifts, schedules
