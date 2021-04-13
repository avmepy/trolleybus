#!/usr/bin/env python3
# -*-encoding: utf-8-*-
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from accounts.models import Profile


def is_driver(user):
    return user.groups.filter(name='Водій').exists()


def is_admin(user):
    return user.groups.filter(name='Адміністратор').exists()


def is_manager(user):
    return user.groups.filter(name='Керівник').exists()


def login_user(request, form):
    """
    login view
    :param request:
    :param form:
    :return:
    """
    cd = form.cleaned_data
    user = authenticate(username=cd['username'], password=cd['password'])
    if user is not None:
        if user.is_active:
            login(request, user)

            if is_admin(request.user):
                return redirect('admin:index')
            elif is_driver(request.user) or is_manager(request.user):
                return redirect('home')
            else:  # for superuser now
                # todo error
                return redirect('admin:index')
        else:
            return HttpResponse('Disabled account')
    else:
        return HttpResponse('Invalid login')


def logout_user(request):
    logout(request)
    return redirect('login')


def get_user_profile(user):

    assert is_driver(user), 'user is not a driver'

    profile = Profile.objects.get(user=user)
    return profile
