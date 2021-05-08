#!/usr/bin/env python3
# -*-encoding: utf-8-*-
from django.contrib.auth.models import User
from routes.models import Shift
from datetime import date


def get_user_shifts(user: User):

    shifts = Shift.objects.filter(driver=user,  date__gte=date.today())
    return shifts
