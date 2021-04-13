#!/usr/bin/env python3
# -*-encoding: utf-8-*-
from django.contrib.auth.models import User
from accounts.models import Profile


def get_user_schedules(user: User):

    profile = Profile.objects.get(user=user)
    schedules = profile.schedules.all()

    # print(schedules, type(schedules))

    return schedules
