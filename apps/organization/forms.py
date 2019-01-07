# -*- coding: utf-8 -*-
from django import forms
from apps.operation.models import UserAsk
import re
# class UserAskForm(forms):
#     name = forms.CharField(required=True,min_length=2,max_length=20)
#     phone = forms.CharField(required=True,min_length=11,max_length=11)
#     course_name = forms.CharField(required=True,min_length=5,max_length=20)

class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REG_MOBIL = r'^1[358]\d{9}$'
        p = re.compile(REG_MOBIL)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号非法',code='mobile_invalid')