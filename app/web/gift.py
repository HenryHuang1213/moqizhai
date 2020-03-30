'''
    -*- coding: utf-8 -*-
    Time : 2020/2/10 11:57
    Author : HenryHuang
    File : gift.py
    Software: PyCharm
'''
__author__ = 'HenryHuang'

from flask import current_app, flash, redirect, url_for, render_template

from . import web
from flask_login import login_required, current_user

from ..libs.enum import PendingStatus
from ..models.base import db
from ..models.drift import Drift
from ..models.gift import Gift
from ..view_models.gift import MyGifts
from ..view_models.trade import MyTrades


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts = view_model.trades)

    # return 'my_gifts'
    # var isbnList = giftsOfMine.map((gift) =>gift.isbn})
    # '' \
    # 'return'
    # return r'Groot said ' ' + "I\'m Groot"

@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))
# def file.open(file, callback)
    # open file
    # callback()
    # close file
# Ture if a ==1  else False
# a == 1?True:False
# @contextmanager
# def


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    gift = Gift.query.filter_by(id=gid, launched = False).first_or_404()
    drift = Drift.query.filter_by(
        gift_id = id, pending = PendingStatus.Waiting).first()
    if drift:
        flash('这个礼物正处于交易状态，请先前往鱼漂完成该交易')
    else:
        with db.auto_commit():
            current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.delete()
    return redirect(url_for('web.my_gifts'))


