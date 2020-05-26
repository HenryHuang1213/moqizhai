'''
    -*- coding: utf-8 -*-
    Time : 2020/2/5 21:47
    Author : HenryHuang
    File : secure.py
    Software: PyCharm
'''
__author__ = 'HenryHuang'


DEBUG = False
# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:huanghe1213henry@localhost:3306/moqizhai'
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:huanghe@mysql2/moqizhai'
# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:huanghe@localhost:3306/moqizhai'
SECRET_KEY = '\xe5\x8f\xa4\xe5\xa5\x95\xe7\x8f\xba\xe6\x98\xaf\xe7\x8c\xaa*4'


MAIL_SERVER = 'smtp.exmail.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'system@moqizhai.com'
MAIL_PASSWORD = 'CHSKTP5bww2KXtBR'
MAIL_SUBJECT_PREFIX = '[moqizhai]'
MAIL_SENDER = 'moqizhai<system@moqizhai.com>'
