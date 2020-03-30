'''
    -*- coding: utf-8 -*- 
    Time : 2020/2/5 9:53 
    Author : HenryHuang
    File : book.py 
    Software: PyCharm
'''
__author__ = 'HenryHuang'

import json

from flask_login import current_user

from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookCollection, BookViewModel
from app.forms.book import SearchForm
from flask import jsonify, request, render_template, flash

from app.view_models.trade import TradeInfo
from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.data_grab import Yushu_Book


@web.route('/book/search/')
def search():

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = Yushu_Book()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)

    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
    return render_template('search_result.html', books=books)



@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False


    # 书籍详情数据
    yushu_book = Yushu_Book()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn = isbn,
                             launched = False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn = isbn,
                             launched = False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched = False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched = False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html', book=book,
                           wishes = trade_wishes_model,
                           gifts = trade_gifts_model,
                           has_in_gifts = has_in_gifts,
                           has_in_wishes = has_in_wishes)



@web.route('/test')
def test():
    r = {
        'name': 'GYJ',
        'age': 18
    }
    flash('hello henry')
    flash('hello GYJ')
    return render_template('test.html', data=r)





