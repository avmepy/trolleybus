#!/usr/bin/env python3
# -*-encoding: utf-8-*-
from django.contrib.auth.models import User
from routes.models import Shift, Schedule


def get_user_shifts_and_schedules(user: User) -> tuple:

    shifts = Shift.objects.filter(driver=user)
    schedules = []
    for shift in shifts:
        schedules += list(shift.schedules)
    print(schedules)
    return shifts, schedules
