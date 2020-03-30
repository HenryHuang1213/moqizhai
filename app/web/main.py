'''
    -*- coding: utf-8 -*-
    Time : 2020/2/10 11:57
    Author : HenryHuang
    File : main.py
    Software: PyCharm
'''
__author__ = 'HenryHuang'

from flask import render_template
from flask_login import login_required, current_user

from . import web
from ..models.gift import Gift
from ..view_models.book import BookViewModel

@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent = books)

@web.route('/personal')
@login_required
def personal_center():
    return render_template('personal.html', user=current_user.summary)

