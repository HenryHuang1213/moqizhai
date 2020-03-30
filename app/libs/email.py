'''
    -*- coding: utf-8 -*- 
    Time : 2020/2/12 10:26 
    Author : HenryHuang
    File : email.py 
    Software: PyCharm
'''
__author__ = 'HenryHuang'

from threading import Thread

from flask import current_app, render_template

from app import mail
from flask_mail import Message

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    # Python email
    # msg = Message('测试邮件', sender= '2329727634@qq.com', body='Test',
    #               recipients=['314267470@qq.com'])
    msg = Message('[墨起斋]' + '' + subject,
                  sender=current_app.config['MAIL_SENDER'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    # current_app  app = Flask()
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    # mail.send(msg)
