'''
    -*- coding: utf-8 -*- 
    Time : 2020/2/5 15:29 
    Author : HenryHuang
    File : __init__.py.py 
    Software: PyCharm
'''
__author__ = 'HenryHuang'

from flask import Blueprint, render_template

web = Blueprint('web',__name__, template_folder='templates')

@web.app_errorhandler(404)
def not_found(e):
    # AOP
    return render_template('404.html'),404

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish







