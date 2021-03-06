# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,min_length=8)

class RegisterForm(forms.Form):
    email=forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=8)
    captcha=CaptchaField()

class ForgetForm(forms.Form):
    email=forms.EmailField(required=True)
    captcha=CaptchaField()

class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=8)
    password2 = forms.CharField(required=True, min_length=8)
