'''
    coding: utf-8
    Time : 2020/2/4
    Author : HenryHuang
    File : fisher.py
    Software: PyCharm
'''
__author__ = 'HenryHuang'

from app import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=app.config['DEBUG'],port=8000)

    # app.run(host='127.0.0.1',debug=True,port=80)

