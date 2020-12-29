# !/usr/bin/env python
# -*- coning: utf-8 -*-
# @Time     : 2019/10/24 9:18
# @Author   : Mr.Gan
# Software  : PyCharm

from common import logconfig
from manage.getconfigparam import *
import requests
import json

# def request(url, param, *args, typed="get"):
#     if typed == "get":
#         response = requests.get(url=url, params=param, timeout=5)
#     elif typed == "post":
#         response = requests.post(url=url, data=param, timeout=5)
#     if response.status_code == 200:
#         if isinstance(response.text, str):
#             text = response.json()
#             code, mes = args
#             if text.get("error_code") == code and text.get("reason") == mes:
#                 return text.get("result")
#             raise ValueError("{} != {} or {} != {}".format(text.get("error_code"), code, text.get("reason"), mes))
#         return response
#     raise ValueError("状态码错误 value=【{}】".format(response.status_code))




def request1(url1,headers1,param1=None, typed="get"):
    if typed == "get":
        if param1 is not None:
            response = requests.get(url=url1,headers=headers1, params=param1)
            return response
        else:
            reresponses=requests.get(url1,headers1)
            return reresponses

    elif typed == "post":
        response= requests.post(url=url1,headers=headers1, json=param1)
        return response





#
# def request1(url1,headers1, param1, typed="get"):
#     if typed == "get":
#         response = requests.get(url=url1,headers=headers1, params=none)
#         if  response.status_code == 200:
#             return response
#         elif response.status_code == 409:
#             return response
#         else:
#             raise ValueError("调用接口失败,状态码为: %s ,返回信息为：%s" % ((response.status_code),response.json()))
#     elif typed == "post":
#         response= requests.post(url=url1,headers=headers1, json=param1)
#         if response.status_code == 200:
#             return response
#         elif response.status_code == 409:
#             return response
#         else:
#             raise ValueError("调用接口失败,状态码为: %s ,返回信息为：%s" % ((response.status_code), response.json()))
