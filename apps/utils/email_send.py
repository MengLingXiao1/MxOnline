# -*- coding: utf-8 -*-
from apps.users.models import EmailVerifyRecord
import random
from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(randomlength):
        str+=random.choice(chars)
    return str


def send_register_email(email,send_type='register'):
    email_recod=EmailVerifyRecord()
    code = random_str(16)
    email_recod.code = code
    email_recod.email = email
    email_recod.send_type = send_type
    email_recod.save()

    email_title = ''
    email_body = ''


    if send_type == 'register':
        email_title = '慕学在线注册激活链接'
        email_body = '请点击下面的链接激活你的账号"http://127.0.0.1:8000/active/{0}'.format(code)


        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])

        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '慕学在线重置密码链接'
        email_body = '请点击下面的链接激活你的账号"http://127.0.0.1:8000/reset/{0}'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])



