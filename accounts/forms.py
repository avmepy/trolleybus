#!/usr/bin/env python3
# -*-encoding: utf-8-*-


from django import forms


class UserLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
