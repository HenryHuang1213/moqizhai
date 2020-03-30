'''
    -*- coding: utf-8 -*- 
    Time : 2020/2/6 11:16 
    Author : HenryHuang
    File : book.py 
    Software: PyCharm
'''
__author__ = 'HenryHuang'


from sqlalchemy import Column, Integer, String

from app.models.base import db


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)  # 主键，自增长
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))    # 装帧版本
    publisher = Column(String(50))  # 出版社
    price = Column(String(20))      # 价格
    pages = Column(Integer)         # 页数
    pubdate = Column(String(20))    # 出版年月
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))  # 简介
    image = Column(String(50))      # 图书图片


    def sample(self):
        pass




