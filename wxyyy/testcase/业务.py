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
import json
from manage.getconfigparam import jh_url

class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        """获取登录的token"""
        url1 = "https://oauthuat.utcook.com/uaa/oauth/login"
        headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
                   "Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "username": "scf_adm",
            "password": "Ut123456",
            "grant_type": "password",
            "scope": "read"
        }
        response = requests.post(url=url1, headers=headers, data=data)
        access_token = response.json()["access_token"]
        Authorization_value = "bearer " + access_token
        global headers1
        headers1 = {
            "Content-Type": "application/json", "Authorization": Authorization_value
        }


        """查询优模型的状态（进行创建之前）"""
        global url
        global chaxun
        url = "https://mobileuat.utcook.com/utmodel"
        """进行查询优模型"""
        # global headers1
        chaxun_url = "https://mobileuat.utcook.com/utmodel/modelAdmin/findProfile"
        chaxun_param = {"category": "ut-device", "identifier": "112"}
        chaxun = requests.get(chaxun_url, headers=headers1, params=chaxun_param)


    def test_01(self):
        if chaxun.json()["utMsg"] :
            print("a")
        """进行判断查询的返回值。不存在有模型的话，直接进行新建优模型。存在的话，进行删除优模型，在进行创建优模型"""
#         global url
#         url="https://mobileuat.utcook.com/utmodel"
#         """进行查询优模型"""
#         # global headers1
#         chaxun_url = "https://mobileuat.utcook.com/utmodel/modelAdmin/findProfile"
#         chaxun_param = {"category": "ut-device", "identifier": "112"}
#         chaxun = request_frame_work.request1(chaxun_url, headers1, chaxun_param)
#         print("——————————————————————查询优模型——————————————————")
#
#         """进行创建优模型"""
#         create_url=url +"/modelAdmin/createProfile"
#         create_param={
#                       "category": "ut-device",
#                       "identifier":"112",
#                       "name":"112",
#                       "description": "更改之前",
#                       "modelSource": "unilink"
#                     }
#         create=request_frame_work.request1(create_url, headers1, create_param,typed="post")
#         print("——————————————————————创建优模型——————————————————")

    """新建属性"""
    create_Property_url = jh_url + "/modelPropertyAdmin/create"
    create_Property_data9=json.dumps(create_Property_data)
    create_Property_data2 = json.loads(create_Property_data)
    create_Property_data2["modelId"] = create
    print(create_Property_data2)
    print(type(create_Property_data2))
    create_Property_data3 = {"modelId": create, "identifier": "shuxing", "name": "属性更改之前", "accessMode": "rw",
                             "dataType": {"specs": {"0": "11", "1": "1"}, "type": "bool"}, "description": "这是描述"}
    print(create_Property_data3)
    print(type(create_Property_data3))
    Property = request_frame_work.request1(create_Property_url, headers1, create_Property_data2, typed="post")
    print(Property)
    print("——————————————————————新建属性——————————————————")
#         """新建属性"""
#         create_Property_url=url +"/modelPropertyAdmin/create"
#         create_Property_data={
#                           "modelId": create,
#                           "identifier": "shuxing",
#                           "name": "属性更改之前",
#                           "accessMode": "rw",
#
#                           "description": "这是描述"
#                         }
#         Property= request_frame_work.request1(create_Property_url, headers1, create_Property_data, typed="post")
#         print("——————————————————————新建属性——————————————————")
#         """新建服务"""
#         create_Service_url = url + "/modelServiceAdmin/create"
#         create_Service_data = {
#             "modelId": create,
#             "identifier": "w20",
#             "name": "服务更改之前",
#             "inputData": [],
#             "outputData": [],
#             "callType": "async",
#             "requestMethod": "delete",
#             "url": "exercitation Duis ex",
#             "description": "65675"
#         }
#         Service = request_frame_work.request1(create_Service_url, headers1, create_Service_data, typed="post")
#         print("——————————————————————新建服务——————————————————")
#         """新建事件"""
#         create_Event_url = url + "/modelEventAdmin/create"
#         create_Event_data = {
#             "modelId": create,
#             "identifier": "13w22",
#             "name": "事件更改之前",
#             "type": "warning",
#             "outputData": [],
#             "description": "描述",
#             "topic": "sed aliqua"
#         }
#         Event = request_frame_work.request1(create_Event_url, headers1, create_Event_data, typed="post")
#         print("——————————————————————新建事件——————————————————")
#         time.sleep(30)
#         """编辑属性"""
#         updata_Property_url = url + "/modelPropertyAdmin/update"
#         updata_Property_data = {
#                       "id": Property,
#                       "property": {
#                         "accessMode": "r",
#                         "dataType": {
#                           "specs": {
#                             "min": -2147483648,
#                             "max": 2147483647,
#                             "step": 2
#                           },
#                           "type": "int"
#                         },
#                         "description": "ipsum occa",
#                         "identifier": "22",
#                         "name": "属性更改之后"
#                       }
#                     }
#         Updata_Property = request_frame_work.request1(updata_Property_url, headers1, updata_Property_data,typed="post")
#         print("——————————————————————编辑属性——————————————————")
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
#         print("——————————————————————编辑事件——————————————————")
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