'''
    coding: utf-8
    Time : 2020/2/4 17:58 
    Author : HenryHuang
    File : http_url_link.py
    Software: PyCharm
'''
__author__ = 'HenryHuang'

# urlib
# requests


import requests


class HTTP:
    '''
        关键字搜索：
        http://t.yushu.im/v2/book/search?q={}&start={}&acount={}
        isbn搜索:
        http://t.yushu.im/v2/book/isbn/{isbn}

        平凡的世界ISBN：
        9787020049295

    '''


    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''













