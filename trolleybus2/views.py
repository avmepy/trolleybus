#!/usr/bin/env python3
# -*-encoding: utf-8-*-
from django.shortcuts import redirect


def start_view(request):
    return redirect('home')
