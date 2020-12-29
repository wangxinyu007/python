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




# def request1(url1,headers1, param1, typed="get"):
#     if typed == "get":
#         response = requests.get(url=url1,headers=headers1, params=param1)
#         if not response.status_code == 200:
#             print("调用接口成功 返回值为 【{}】".format(response.text))
#             return response.text
#         else:
#             raise ValueError("调用接口失败的原因为 【{}】".format(response.json()))
#     elif typed == "post":
#         response= requests.post(url=url1,headers=headers1, json=param1)
#         if response.status_code == 200:
#             print("调用接口成功 返回值为 【{}】".format(response.text))
#             return response.text
#         else:
#             raise ValueError("调用接口失败的原因为 【{}】".format(response.json()["utMsg"]))







def request1(url1,headers1,param1=None, typed="get"):
    if typed == "get":
        if param1 is not None:
            response = requests.get(url=url1,headers=headers1, params=param1)
            return response
        else:
            reresponses=requests.get(url1,headers1)
            return reresponses

    elif typed == "post":
        response= requests.post(url=url1,headers=headers1, data=param1)
        return response

#
# def create_updata_check_delete_check(create_Property_url,create_Property_data,updata_Property_url,updata_Property_data,chaxun_Property_url,delete_Property_url):
#         """新建属性"""
#         # create_Property_url = jh_url + "/modelPropertyAdmin/create"
#         create_Property_data2 = json.loads(create_Property_data)
#         create_Property_data2["modelId"] = create.text
#         Property = request_frame_work.request1(create_Property_url, headers1, create_Property_data2, typed="post")
#         self.assertEqual(200, Property.status_code, "调用  新建属性  接口失败。状态码错误")
#         if "utMsg" in Property.text:
#             raise ValueError("调用  新建属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Property.status_code), Property.json()))
#         """编辑属性"""
#         updata_Property_url = jh_url + "/modelPropertyAdmin/update"
#         updata_Property_data2 = json.loads(updata_Property_data)
#         updata_Property_data2["id"] = Property.text
#         Updata_Property = request_frame_work.request1(updata_Property_url, headers1, updata_Property_data2,typed="post")
#         self.assertEqual(200, Updata_Property.status_code, "调用  编辑属性  接口失败。状态码错误")
#         if "utMsg" in Updata_Property.text:
#             raise ValueError("调用  修改属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Property.status_code), Updata_Property.json()))
#
#         """查询属性"""
#         chaxun_Property_url = jh_url + "/modelPropertyAdmin/find"
#         Property_data = {"id": Property.text}
#         chaxun_Property = request_frame_work.request1(chaxun_Property_url, headers1, Property_data)
#         self.assertEqual(200, chaxun_Property.status_code, "调用  查询属性  接口失败。状态码错误")
#         if "utMsg" in chaxun_Property.text:
#             raise ValueError("调用  修改属性  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Property.status_code), chaxun_Property.json()))
#         elif "name" in chaxun_Property.text:
#             if not "修改属性之后" == chaxun_Property.json()["name"]:
#                 raise ValueError("修改属性失败，错误原因为 : %s " % (chaxun_Property.json()))
#
#         """删除属性"""
#         delete_Property_url = jh_url + "/modelPropertyAdmin/delete"
#         delete_Property_data = Property.text
#         Delete_Property = requests.post(url=delete_Property_url, headers=headers1, data=delete_Property_data)
#         self.assertEqual(200, Delete_Property.status_code, "调用  删除属性  接口失败。状态码错误")
#         if  not "utMsg" in Delete_Property.text:
#             raise ValueError("调用  删除属性接口失败  原因为 【{}】".format(Delete_Property.json()["utMsg"]))
#
#         """查询属性"""
#         chaxun_delete_Property_url = jh_url + "/modelPropertyAdmin/find"
#         Property_delete_data = {"id": Property.text}
#         chaxun_delete_Property = request_frame_work.request1(chaxun_delete_Property_url, headers1, Property_delete_data)
#         self.assertEqual(200, chaxun_Property.status_code, "调用  查询属性  接口失败。状态码错误")
#         if "utMsg" in chaxun_Property.text:
#             raise ValueError("调用  查询属性  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_delete_Property.status_code), chaxun_delete_Property.json()))




        #     print("调用接口成功 返回值为 【{}】".format(response.text))
        #     return response.text
        # else:
        #     raise ValueError("调用接口失败的原因为 【{}】".format(response.json()["utMsg"]))










# def request1(url1,headers1, param1, typed="get"):
#     if typed == "get":
#         response = requests.get(url=url1,headers=headers1, params=param1)
#         if response.status_code == 200:
#             print("调用接口成功 返回值为 【{}】".format(response.text))
#             return response.text
#         else:
#             print("调用接口失败的原因为 【{}】".format(response.json()["utMsg"]))
#             return response.json()["utMsg"]
#     elif typed == "post":
#         response= requests.post(url=url1,headers=headers1, json=param1)
#         if response.status_code == 200:
#             print("调用接口成功 返回值为 【{}】".format(response.text))
#             return response.text
#         else:
#             print("调用接口失败的原因为 【{}】".format(response.json()["utMsg"]))
#             return response.json()["utMsg"]

