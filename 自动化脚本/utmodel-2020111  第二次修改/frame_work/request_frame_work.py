# !/usr/bin/env python
# -*- coning: utf-8 -*-
# @Time     : 2019/10/24 9:18
# @Author   : Mr.Gan
# Software  : PyCharm

from common import logconfig
from manage.getconfigparam import *
import requests
import json
from  manage.getconfigparam import *
logs = logconfig.SetLog()
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




def response1(response2,name1,name2):
    if "utMsg" in response2.text:
        logs.error(name1+"  :状态码为: %s ,返回信息为：%s" % ((response2.status_code), response2.json()["utMsg"]))
    else:
        logs.info(name2)

def response2(response3,name3,name4,name5):
    if "utMsg" in response3.text:
        logs.error(name3+"  : 状态码为:%s ,返回信息为：%s" % ((response3.status_code), response3.json()["utMsg"]))
    else:
        if "修改之后" != response3.json()["description"]:
            logs.error(name4+"  :状态码为: %s ,返回信息为：%s" % ((response3.status_code), response3.json()["description"]))
        else:
            logs.info(name5)

def response3(response6,name7,name8):
    if "utMsg" in response6.text:
        logs.info(name8)
    else:
        logs.error(name7+"  :状态码为: %s ,返回信息为：%s" % ((response6.status_code), response6.json()["utMsg"]))
        raise ValueError(name7+  "  :状态码为: %s ,返回信息为：%s" % ((response6.status_code), response6.json()["utMsg"]))

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
