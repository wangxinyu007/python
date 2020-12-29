# !/usr/bin/env python
# -*- coning: utf-8 -*-
# @Time     : 2019/10/23 14:28
# @Author   : Mr.Gan
# Software  : PyCharm



import unittest
import unittest
from frame_work import request_frame_work
import requests
import time
from common import logconfig
from manage.getconfigparam import *
import json


class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        """获取登录的token"""
        url1 = "https://oauthuat.utcook.com/uaa/oauth/login"
        headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
                   "Content-Type": "application/x-www-form-urlencoded"}
        login_data1=json.loads(login_data)
        response = requests.post(url=url1, headers=headers, data=login_data1)
        access_token = response.json()["access_token"]
        Authorization_value = "bearer " + access_token
        global headers1
        headers1 = {
            "Content-Type": "application/json", "Authorization": Authorization_value
        }
        """进行查询优模型"""
        global chaxun
        chaxun_url = jh_url + "/modelAdmin/findProfile"
        chaxun_param12=json.loads(chaxun_param)
        chaxun = request_frame_work.request1(chaxun_url, headers1, chaxun_param12)

    def test_01(self):
        """进行判断，如果没有报错信息。说明优模型存在，进行删除优模型，
                     如果有报错信息，说明没有优模型存在，进行创建优模型"""
        if "utMsg" not in chaxun.json():
            delete_url = jh_url + "/modelAdmin/delete"
            chaxun_param2 = json.loads(chaxun_param)
            delete = request_frame_work.request1(delete_url, headers1, chaxun_param2,typed="post")
            self.assertEqual(200, delete.status_code, "调用  删除优模型  接口失败。状态码错误")
            if "utMsg"  in delete.text:
                raise ValueError("调用   删除优模型接口  失败,状态码为: %s ,返回信息为：%s" % ((delete.status_code), delete.json()))

        """进行创建优模型"""
        create_url=jh_url +"/modelAdmin/createProfile"
        create_param1 = json.loads(create_param)
        create=request_frame_work.request1(create_url, headers1, create_param1,typed="post")
        self.assertEqual(200, create.status_code, "调用  进行创建优模型  接口失败。状态码错误")

        """新建属性"""
        create_Property_url=jh_url +"/modelPropertyAdmin/create"
        create_Property_data2=json.loads(create_Property_data)
        create_Property_data2["modelId"]=create.text
        Property= request_frame_work.request1(create_Property_url, headers1, create_Property_data2, typed="post")
        self.assertEqual(200, Property.status_code, "调用  新建属性  接口失败。状态码错误")
        if "utMsg"  in Property.text:
            raise ValueError("调用  新建属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Property.status_code), Property.json()))

        """新建服务"""
        create_Service_url = jh_url + "/modelServiceAdmin/create"
        create_Service_data2 = json.loads(create_Service_data)
        create_Service_data2["modelId"] = create.text
        Service = request_frame_work.request1(create_Service_url, headers1, create_Service_data2, typed="post")
        self.assertEqual(200, Service.status_code, "调用  新建服务  接口失败。状态码错误")
        if "utMsg"  in Service.text:
            raise ValueError("调用  新建属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Service.status_code), Service.json()))

        """新建事件"""
        create_Event_url = jh_url + "/modelEventAdmin/create"
        create_Event_data2 = json.loads(create_Event_data)
        create_Event_data2["modelId"] = create.text
        Event = request_frame_work.request1(create_Event_url, headers1, create_Event_data2, typed="post")
        self.assertEqual(200, Event.status_code, "调用  新建事件  接口失败。状态码错误")
        if "utMsg"  in Event.text:
            raise ValueError("调用  新建属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Event.status_code), Event.json()))

        """编辑属性"""
        updata_Property_url = jh_url + "/modelPropertyAdmin/update"
        updata_Property_data2 = json.loads(updata_Property_data)
        updata_Property_data2["id"] = Property.text
        Updata_Property = request_frame_work.request1(updata_Property_url, headers1, updata_Property_data2,typed="post")
        self.assertEqual(200, Updata_Property.status_code, "调用  编辑属性  接口失败。状态码错误")
        if "utMsg"  in Updata_Property.text:
            raise ValueError("调用  修改属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Property.status_code), Updata_Property.json()))

        """查询属性"""
        chaxun_Property_url=jh_url+ "/modelPropertyAdmin/find"
        Property_data={"id":Property.text}
        chaxun_Property= request_frame_work.request1(chaxun_Property_url, headers1, Property_data)
        self.assertEqual(200, chaxun_Property.status_code, "调用  查询属性  接口失败。状态码错误")
        if "utMsg"  in chaxun_Property.text:
            raise ValueError("调用  修改属性  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Property.status_code), chaxun_Property.json()))
        elif "name"  in chaxun_Property.text:
            if not "修改属性之后" == chaxun_Property.json()["name"]:
                raise ValueError("修改属性失败，错误原因为 : %s " % (chaxun_Property.json()))

        """删除属性"""
        delete_Property_url=jh_url+ "/modelPropertyAdmin/delete"
        delete_Property_data = Property.text
        Delete_Property = requests.post(url=delete_Property_url, headers=headers1, data=delete_Property_data)
        self.assertEqual(200, Delete_Property.status_code, "调用  删除属性  接口失败。状态码错误")
        if "utMsg" in Delete_Property.text:
            raise ValueError("调用  删除属性接口   失败的原因为 【{}】".format(Delete_Property.json()["utMsg"]))

        """编辑服务"""
        updata_Service_url = jh_url + "/modelServiceAdmin/update"
        updata_Service_data2 = json.loads(updata_Service_data)
        updata_Service_data2["id"] = Service.text
        Updata_Service = request_frame_work.request1(updata_Service_url, headers1, updata_Service_data2,typed="post")
        self.assertEqual(200, Updata_Service.status_code, "调用  编辑服务  接口失败。状态码错误")
        if "utMsg" in Updata_Service.text:
            raise ValueError(
                "调用  修改服务  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Service.status_code), Updata_Service.json()))

        """查询服务"""
        chaxun_Service_url = jh_url + "/modelServiceAdmin/find"
        Service_data = {"id": Service.text}
        chaxun_Service = request_frame_work.request1(chaxun_Service_url, headers1, Service_data)
        self.assertEqual(200, chaxun_Service.status_code, "调用  查询服务  接口失败。状态码错误")
        if "utMsg" in chaxun_Service.text:
            raise ValueError(
                "调用  修改服务  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Service.status_code), chaxun_Service.json()))
        elif "name" in chaxun_Service.text:
            if not "修改服务之后" == chaxun_Service.json()["name"]:
                raise ValueError("修改服务失败，错误原因为 : %s " % (chaxun_Service.json()))

        """编辑事件"""
        updata_Event_url = jh_url + "/modelEventAdmin/update"
        updata_Event_data2 = json.loads(updata_Event_data)
        updata_Event_data2["id"] = Event.text
        Updata_Event = request_frame_work.request1(updata_Event_url, headers1, updata_Event_data2,typed="post")
        self.assertEqual(200, Updata_Event.status_code, "调用  编辑事件  接口失败。状态码错误")
        if "utMsg" in Updata_Event.text:
            raise ValueError(
                "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Event.status_code), Updata_Event.json()))

        """查询事件"""
        chaxun_Event_url = jh_url + "/modelEventAdmin/find"
        Event_data = {"id": Event.text}
        chaxun_Event = request_frame_work.request1(chaxun_Event_url, headers1, Event_data)
        self.assertEqual(200, chaxun_Event.status_code, "调用  查询事件  接口失败。状态码错误")
        if "utMsg" in chaxun_Event.text:
            raise ValueError(
                "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Event.status_code), chaxun_Event.json()))
        elif "name" in chaxun_Event.text:
            if not "修改事件之后" == chaxun_Event.json()["name"]:
                raise ValueError("修改事件失败，错误原因为 : %s " % (chaxun_Event.json()))

        """编辑优模型"""
        updata_url = jh_url + "/modelAdmin/updateProfile"
        updata_param2 = json.loads(updata_param)
        # updata_param2["id"] = Event.text
        Updata_model = request_frame_work.request1(updata_url, headers1, updata_param2, typed="post")
        self.assertEqual(200, Updata_model.status_code, "调用  编辑优模型  接口失败。状态码错误")
        if "utMsg" in Updata_model.text:
            raise ValueError(
                "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_model.status_code), Updata_model.json()))

        """查询被修改的优模型"""
        chaxun_updata_model_url = jh_url + "/modelAdmin/findProfile"
        chaxun_updata_model_param12 = json.loads(chaxun_param)
        chaxun_updata_model = request_frame_work.request1(chaxun_updata_model_url, headers1, chaxun_updata_model_param12)
        self.assertEqual(200, chaxun_updata_model.status_code, "调用  查询被修改的优模型  接口失败。状态码错误")
        if "utMsg" in chaxun_updata_model.text:
            raise ValueError(
                "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_updata_model.status_code), chaxun_updata_model.json()))
        elif "name" in chaxun.text:
            if not "修改之后" == chaxun_updata_model.json()["description"]:
                raise ValueError("修改优模型失败，错误原因为 : %s " % (chaxun_updata_model.json()))

        # """删除优模型"""
        # delete_updata_model_url = jh_url + "/modelAdmin/delete"
        # delete_updata_model2 = json.loads(chaxun_param)
        # delete_updata_model = request_frame_work.request1(delete_updata_model_url, headers1, delete_updata_model2, typed="post")
        # self.assertEqual(200, delete_updata_model.status_code, "调用  删除优模型  接口失败。状态码错误")
        # if "utMsg" in delete_updata_model.text:
        #     raise ValueError("调用   删除优模型接口  失败,状态码为: %s ,返回信息为：%s" % ((delete_updata_model.status_code), delete_updata_model.json()))
        # """查询被删除优模型"""
        # chaxun_delete_model_url = jh_url + "/modelAdmin/findProfile"
        # chaxun_delete_model_param12 = json.loads(chaxun_param)
        # chaxun_delete_model = request_frame_work.request1(chaxun_delete_model_url, headers1,chaxun_delete_model_param12)
        # # if not "无效的分类或标识符" == chaxun_delete_model.json()["utMsg"]:
        # #     raise ValueError("调用  查询被删除的优模型  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_delete_model.status_code), chaxun_delete_model.json()))
        # self.assertEqual(409, chaxun_delete_model.status_code, "调用  查询被删除的优模型  接口失败。状态码错误")
        # self.assertEqual("无效的分类或标识符",chaxun_delete_model.json()["utMsg"], "返回信息不匹配")


































#         """编辑服务"""
#         updata_Service_url = url + "/modelServiceAdmin/update"
#         updata_Service_data = {
#             "id": Service,
#             "service": {
#                 "callType": "async",
#                 "description": "et officia qui ullamco tempor",
#                 "identifier": "111dd11111",
#                 "inputData": [],
#                 "name": "服务更改之后",
#                 "outputData": [],
#                 "requestMethod": "fffpppput",
#                 "url": "1"
#             }
#         }
#         Updata_Service = request_frame_work.request1(updata_Service_url, headers1, updata_Service_data, typed="post")
#         print("——————————————————————编辑服务——————————————————")
#         """编辑事件"""
#         updata_Event_url = url + "/modelEventAdmin/update"
#         updata_Event_data = {"id": Event,
#                              "event": {
#                                  "description": "aute ut id",
#                                  "identifier": "ss",
#                                  "type": "warning",
#                                  "name": "事件更改之后",
#                                  "outputData": [],
#                                  "topic": "dolore"
#                              }
#                              }
#         Updata_Event = request_frame_work.request1(updata_Event_url, headers1, updata_Event_data, typed="post")
#         print("——————————————————————编辑事件——————————————————")
#         time.sleep(30)
#         """删除属性"""
#         delete_Property_url = url + "/modelPropertyAdmin/delete"
#         delete_Property_data = Property
#         Delete_Property = requests.post(url=delete_Property_url,headers=headers1, data=delete_Property_data)
#         if Delete_Property.status_code == 200:
#             print("调用接口成功 返回值为 【{}】".format(Delete_Property.text))
#         else:
#             raise ValueError("调用接口失败的原因为 【{}】".format(Delete_Property.json()["utMsg"]))
#         print("——————————————————————删除属性——————————————————")
#         """删除服务"""
#         delete_Service_url = url + "/modelServiceAdmin/delete"
#         delete_Service_data = Service
#         Delete_Service = requests.post(url=delete_Service_url, headers=headers1, data=delete_Service_data)
#         if Delete_Service.status_code == 200:
#             print("调用接口成功 返回值为 【{}】".format(Delete_Property.text))
#         else:
#             raise ValueError("调用接口失败的原因为 【{}】".format(Delete_Property.json()["utMsg"]))
#         print("——————————————————————删除服务——————————————————")
#         """删除事件"""
#         delete_Event_url = url + "/modelEventAdmin/delete"
#         delete_Event_data = Event
#         Delete_Event = requests.post(url=delete_Event_url, headers=headers1, data=delete_Event_data)
#         if Delete_Event.status_code == 200:
#             print("调用接口成功 返回值为 【{}】".format(Delete_Property.text))
#         else:
#             raise ValueError("调用接口失败的原因为 【{}】".format(Delete_Property.json()["utMsg"]))
#         print("——————————————————————删除事件——————————————————")
#         time.sleep(30)
#         """编辑优模型"""
#         updata_url = url + "/modelAdmin/updateProfile"
#         updata_data = {
#                       "category": "ut-device",
#                       "identifier": "112",
#                       "description": "更改之后"
#                     }
#         Updata = request_frame_work.request1(updata_url, headers1, updata_data, typed="post")
#         print("——————————————————————编辑优模型——————————————————")
#         time.sleep(30)
#         """删除优模型"""
#         delete_url = url + "/modelAdmin/delete"
#         delete_data = {
#               "category": "ut-device",
#               "identifier": "112"
# }
#         delete = request_frame_work.request1(delete_url, headers1, delete_data, typed="post")
#         print("——————————————————————删除优模型——————————————————")

    # """新建服务"""
    # create_Service_url = url + "/modelServiceAdmin/create"
    # create_Service_data = {
    #     "modelId": create,
    #     "identifier": "w20",
    #     "name": "92w",
    #     "inputData": [],
    #     "outputData": [],
    #     "callType": "async",
    #     "requestMethod": "delete",
    #     "url": "exercitation Duis ex",
    #     "description": "65675"
    # }
    # Service = request_frame_work.request1(create_Service_url, headers1, create_Service_data, typed="post")
    # print("——————————————————————新建服务——————————————————")
    # """编辑服务"""
    # updata_Service_url = url + "/modelServiceAdmin/update"
    # updata_Service_data = {
    #               "id": Service,
    #               "service": {
    #                 "callType": "async",
    #                 "description": "et officia qui ullamco tempor",
    #                 "identifier": "111dd11111",
    #                 "inputData": [],
    #                 "name":"7777777",
    #                 "outputData": [],
    #                 "requestMethod": "fffpppput",
    #                 "url": "1"
    #               }
    #             }
    # Updata_Service = request_frame_work.request1(updata_Service_url, headers1, updata_Service_data, typed="post")
    # print("——————————————————————编辑服务——————————————————")
    # """删除服务"""
    # delete_Service_url = url + "/modelServiceAdmin/delete"
    # delete_Service_data = Service
    # Delete_Service = requests.post(url=delete_Service_url, headers=headers1, data=delete_Service_data)
    # if Delete_Service.status_code == 200:
    #     print("调用接口成功 返回值为 【{}】".format(Delete_Property.text))
    # else:
    #     raise ValueError("调用接口失败的原因为 【{}】".format(Delete_Property.json()["utMsg"]))
    # print("——————————————————————删除服务——————————————————")
    # """新建事件"""
    # create_Event_url = url + "/modelEventAdmin/create"
    # create_Event_data = {
    #     "modelId": create,
    #     "identifier": "13w22",
    #     "name": "122w3",
    #     "type": "warning",
    #     "outputData": [],
    #     "description": "描述",
    #     "topic": "sed aliqua"
    # }
    # Event = request_frame_work.request1(create_Event_url, headers1, create_Event_data, typed="post")
    # print("——————————————————————新建事件——————————————————")
    # """编辑事件"""
    # updata_Event_url = url + "/modelEventAdmin/update"
    # updata_Event_data = {"id": Event,
    #                   "event": {
    #                     "description": "aute ut id",
    #                     "identifier": "ss",
    #                     "type": "warning",
    #                     "name": "72",
    #                     "outputData": [],
    #                     "topic": "dolore"
    #                   }
    #                 }
    # Updata_Event= request_frame_work.request1(updata_Event_url, headers1, updata_Event_data, typed="post")
    # print("——————————————————————编辑事件——————————————————")
    # # """删除事件"""
    # # delete_Event_url = url + "/modelEventAdmin/delete"
    # # delete_Event_data = Event
    # # Delete_Event = requests.post(url=delete_Event_url, headers=headers1, data=delete_Event_data)
    # # if Delete_Event.status_code == 200:
    # #     print("调用接口成功 返回值为 【{}】".format(Delete_Property.text))
    # # else:
    # #     raise ValueError("调用接口失败的原因为 【{}】".format(Delete_Property.json()["utMsg"]))
    # # print("——————————————————————删除事件——————————————————")

















    # def test_01(self):
    #     url = "https://oauthuat.utcook.com/uaa/oauth/login"
    #     headers={"Authorization":"Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0","Content-Type":"application/x-www-form-urlencoded"}
    #     data = {
    #         "username":"scf_adm",
    #         "password":"Ut123456",
    #         "grant_type":"password",
    #         "scope":"read"
    #     }
    #     response = requests.post(url=url, headers=headers,data=data)
    #     # print(response.text)
    #     access_token=response.json()["access_token"]
    #     # print(access_token)
    #
    #     url1="https://mobileuat.utcook.com/utmodel/modelAdmin/createProfile"
    #     data1={
    #             "category": "ut-device",
    #             "identifier": "41j2221",
    #             "name": "411j3122",
    #             "description": "中文aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    #             "modelSource": "unilink"
    #         }
    #     Authorization_value="bearer " + access_token
    #     header={
    #         "Content-Type":"application/json",
    #         "Authorization":Authorization_value
    #     }
    #     create1=requests.post(url=url1,headers=header,data=data1)
    #     print(header)
    #     print(data1)
    #     print(create1.text)



    def tearDown(self) -> None:
        pass