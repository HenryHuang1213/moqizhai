'''
    -*- coding: utf-8 -*- 
    Time : 2020/2/10 16:10 
    Author : HenryHuang
    File : wish.py 
    Software: PyCharm
'''
__author__ = 'HenryHuang'

from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.data_grab import Yushu_Book


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid =Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid =Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        # 根据传入的一组isbn，到Wish表中
        # 计算出某个礼物的gift心愿数量
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = Yushu_Book()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first


from app.models.gift import Gift