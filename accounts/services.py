#!/usr/bin/env python3
# -*-encoding: utf-8-*-
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect


def is_driver(user):
    return user.groups.filter(name='Водій').exists()


def is_admin(user):
    return user.groups.filter(name='Адміністратор').exists()


def is_manager(user):
    return user.groups.filter(name='Керівник').exists()


def login_user(request, form):
    cd = form.cleaned_data
    user = authenticate(username=cd['username'], password=cd['password'])
    if user is not None:
        if user.is_active:
            login(request, user)

            if is_admin(request.user):
                return redirect('admin:index')
            else:
                return redirect('home')
        else:
            return HttpResponse('Disabled account')
    else:
        return HttpResponse('Invalid login')


def logout_user(request):
    logout(request)
    return redirect('login')
