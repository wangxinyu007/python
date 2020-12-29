# !/usr/bin/env python
# -*- coning: utf-8 -*-
# @Author   : Mr.王
# Software  : PyCharm
import unittest
from frame_work import request_frame_work
import requests
from manage.getconfigparam import *
import json
import unittest
from ddt import ddt, data, file_data, unpack
import pytest
import allure
from common import tokrn
from common import logconfig
from manage.getconfigparam import *

logs = logconfig.SetLog()
"""整体业务流程
    test'01
        查询优模型   不存在---------------新建优模型
        查询优模型  存在----删除优模型---新建优模型 ---新建 /服务/事件/属性---编辑/服务/事件/属性----查询/服务/事件/属性（是否编辑成功）----删除/服务/事件/属性----在查询/服务/事件/属性（是否删除成功）---编辑优模型----查询优模型（是否编辑成功）-----删除优模型-----查询优模型（是否删除成功）                   

    test02
    查询优模型  不存在  -----用过导入创建优模型-查询优模型
                存在   -----  第一次导入修改优模型  --- 查询优模型 --- 第二次导入修改优模型 ----查询优模型
                导入，导入查询两次。为了保证导入修改优模型成功。
"""
import warnings


@allure.feature('')
class MyTest(unittest.TestCase):

    def setUp(self) -> None:

        global old_description
        old_description = "修改之前"
        global new_description
        new_description = "修改之后"

        # 去除警告
        warnings.simplefilter("ignore", ResourceWarning)

        """获取登录的token"""
        global headers1
        headers1 = tokrn.get_token()

    @allure.story('新建优模型')
    def test_01(self):
        """('新建优模型')"""
        logs.info("----------------------------------------------test1------------------------------------------------")
        """进行查询优模型，有优模型进行删除。没有优模型不操作"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        # 进行序列化
        getmodel_param2 = json.loads(getmodel_param)
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
        if "utMsg" in getModelProfileByKeyUsingGET.json():
            logs.info("查询不到优模型，暂时不操作，结束if循环之后进行创建优模型")
        else:
            """查询到优模型，说明有优模型存在，进行删除优模型"""
            deleteModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/delete"
            delete_param2 = json.loads(getmodel_param)
            deleteModelProfileByKeyUsingPOST = request_frame_work.request1(deleteModelProfileByKeyUsingPOST_url,headers1, delete_param2, typed="post")
            self.assertEqual(200, deleteModelProfileByKeyUsingPOST.status_code, "调用--删除优模型--接口失败。")
            logs.info("查询到优模型，说明有优模型存在，进行删除优模型。")

        """创建优模型"""
        createModelProfileUsingPOST_url = jh_url + "/modelAdmin/createProfile"
        create_param1 = json.loads(create_param)
        create_param1["description"] = old_description
        createModelProfileUsingPOST = request_frame_work.request1(createModelProfileUsingPOST_url, headers1,
                                                                  create_param1, typed="post")
        # self.assertEqual(200, createModelProfileUsingPOST.status_code, "调用--进行创建优模型--接口失败。")
        request_frame_work.response1(createModelProfileUsingPOST, "无法创建优模型", "创建优模型成功")

        print(
            "----------------------------------------------------------属性----------------------------------------------------------")
        """新建属性"""
        createThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/create"
        create_Property_data2 = json.loads(create_Property_data)
        create_Property_data2["modelId"] = createModelProfileUsingPOST.text
        createThingPropertyUsingPOST = request_frame_work.request1(createThingPropertyUsingPOST_url, headers1,create_Property_data2, typed="post")
        # self.assertEqual(200, createThingPropertyUsingPOST.status_code, "调用--进行创建优模型--接口失败。")
        request_frame_work.response1(createThingPropertyUsingPOST, "无法创建属性", "创建属性成功")

        """修改属性"""
        updateThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/update"
        updata_Property_data2 = json.loads(updata_Property_data)
        updata_Property_data2["id"] = createThingPropertyUsingPOST.text
        updata_Property_data2["property"]["description"] = new_description
        updateThingPropertyUsingPOST = request_frame_work.request1(updateThingPropertyUsingPOST_url, headers1,updata_Property_data2, typed="post")
        # self.assertEqual(200, updateThingPropertyUsingPOST.status_code, "调用--进行创建优模型--接口失败。")
        request_frame_work.response1(updateThingPropertyUsingPOST, "无法修改属性", "调用修改属性接口成功")

        """查询属性"""
        findThingPropertyUsingGET_url = jh_url + "/modelPropertyAdmin/find"
        findThingPropertyUsingGET_data = {"id": createThingPropertyUsingPOST.text}
        findThingPropertyUsingGET = request_frame_work.request1(findThingPropertyUsingGET_url, headers1, findThingPropertyUsingGET_data)
        # self.assertEqual(200, findThingPropertyUsingGET.status_code, "调用--查询属性--接口失败。")
        request_frame_work.response2(findThingPropertyUsingGET, "无法查询属性", "修改属性失败", "属性已被修改")

        """删除属性"""
        deleteThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/delete"
        deleteThingPropertyUsingPOST_data = createThingPropertyUsingPOST.text
        deleteThingPropertyUsingPOST = requests.post(url=deleteThingPropertyUsingPOST_url, headers=headers1,
                                                     data=deleteThingPropertyUsingPOST_data)
        # self.assertEqual(200, deleteThingPropertyUsingPOST.status_code, "调用--删除属性--接口失败。状态码错误")
        request_frame_work.response1(deleteThingPropertyUsingPOST, "无法删除属性", "调用删除属性接口成功")

        """查询被删除的属性"""
        findThingPropertyUsingGET_url = jh_url + "/modelPropertyAdmin/find"
        findThingPropertyUsingGET_data = {"id": createThingPropertyUsingPOST.text}
        findThingPropertyUsingGET = request_frame_work.request1(findThingPropertyUsingGET_url, headers1,
                                                                findThingPropertyUsingGET_data)
        # self.assertEqual(200, findThingPropertyUsingGET.status_code, "调用--查询属性--接口失败。")
        request_frame_work.response3(findThingPropertyUsingGET, "无法查询属性", "属性已被删除")

        print(
            "----------------------------------------------------------服务----------------------------------------------------------")
        """新建服务"""
        createThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/create"
        create_Service_data2 = json.loads(create_Service_data)
        create_Service_data2["modelId"] = createModelProfileUsingPOST.text
        createThingServiceUsingPOST = request_frame_work.request1(createThingServiceUsingPOST_url, headers1,
                                                                  create_Service_data2, typed="post")
        request_frame_work.response1(createThingServiceUsingPOST, "无法创建服务", "创建属性服务")

        """修改服务"""
        updateThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/update"
        updata_Service_data2 = json.loads(updata_Service_data)
        updata_Service_data2["id"] = createThingServiceUsingPOST.text
        updata_Service_data2["service"]["description"] = new_description
        updateThingServiceUsingPOST = request_frame_work.request1(updateThingServiceUsingPOST_url, headers1,
                                                                  updata_Service_data2, typed="post")
        request_frame_work.response1(updateThingServiceUsingPOST, "无法修改服务", "调用修改服务接口成功")

        """查询服务"""
        findThingServiceUsingGET_url = jh_url + "/modelServiceAdmin/find"
        findThingServiceUsingGET_data = {"id": createThingServiceUsingPOST.text}
        findThingServiceUsingGET = request_frame_work.request1(findThingServiceUsingGET_url, headers1,
                                                               findThingServiceUsingGET_data)
        request_frame_work.response2(findThingServiceUsingGET, "无法查询服务", "修改服务失败", "服务已被修改")

        """删除服务"""
        deleteThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/delete"
        deleteThingServiceUsingPOST_data = createThingServiceUsingPOST.text
        deleteThingServiceUsingPOST = requests.post(url=deleteThingServiceUsingPOST_url, headers=headers1,
                                                    data=deleteThingServiceUsingPOST_data)
        request_frame_work.response1(deleteThingServiceUsingPOST, "无法删除服务", "调用删除服务接口成功")

        """查询被删除的服务"""
        findThingServiceUsingGET_url = jh_url + "/modelServiceAdmin/find"
        findThingServiceUsingGET_data = {"id": createThingServiceUsingPOST.text}
        findThingServiceUsingGET = request_frame_work.request1(findThingServiceUsingGET_url, headers1,
                                                               findThingServiceUsingGET_data)
        # self.assertEqual(200, findThingPropertyUsingGET.status_code, "调用--查询属性--接口失败。")
        request_frame_work.response3(findThingServiceUsingGET, "无法查询服务", "服务已被删除")

        print(
            "----------------------------------------------------------事件----------------------------------------------------------")
        """新建事件"""
        createThingEventUsingPOST_url = jh_url + "/modelEventAdmin/create"
        create_Event_data2 = json.loads(create_Event_data)
        # create_Event_data2["modelId"] = createModelProfileUsingPOST.text
        create_Event_data2["modelId"] = "1212"
        createThingEventUsingPOST = request_frame_work.request1(createThingEventUsingPOST_url, headers1,create_Event_data2, typed="post")
        self.assertEqual(200, createThingEventUsingPOST.status_code, "调用  编辑事件  接口失败。状态码错误")
        request_frame_work.response1(createThingEventUsingPOST, "无法创建事件", "创建属性事件")

        """修改事件"""
        updateThingEventUsingPOST_url = jh_url + "/modelEventAdmin/update"
        updata_Event_data2 = json.loads(updata_Event_data)
        updata_Event_data2["id"] = createThingEventUsingPOST.text
        updata_Event_data2["event"]["description"] = "asdasdad"
        updateThingEventUsingPOST = request_frame_work.request1(updateThingEventUsingPOST_url, headers1,updata_Event_data2, typed="post")
        # self.assertEqual(200, updateThingEventUsingPOST.status_code, "调用  编辑事件  接口失败。状态码错误")
        request_frame_work.response1(updateThingEventUsingPOST, "无法修改事件", "调用修改事件接口成功")


        """查询事件"""
        findThingEventUsingGET_url = jh_url + "/modelEventAdmin/find"
        findThingEventUsingGET_data1 = {"id": createThingEventUsingPOST.text}
        findThingEventUsingGET = request_frame_work.request1(findThingEventUsingGET_url, headers1,findThingEventUsingGET_data1)
        print(findThingEventUsingGET.text)

        request_frame_work.response2(findThingEventUsingGET, "无法查询事件", "修改服务事件", "事件已被修改")

        """删除事件"""
        deleteThingEventUsingPOST_url = jh_url + "/modelEventAdmin/delete"
        deleteThingEventUsingPOST_data = createThingEventUsingPOST.text
        deleteThingEventUsingPOST = requests.post(url=deleteThingEventUsingPOST_url, headers=headers1, data=deleteThingEventUsingPOST_data)
        request_frame_work.response1(deleteThingEventUsingPOST, "无法删除事件", "调用删除事件接口成功")

        """查询被删除的事件"""
        findThingEventUsingGET_url = jh_url + "/modelEventAdmin/find"
        findThingEventUsingGET_data = {"id": createThingEventUsingPOST.text}
        findThingEventUsingGET = request_frame_work.request1(findThingEventUsingGET_url, headers1,findThingEventUsingGET_data)
        # self.assertEqual(200, findThingPropertyUsingGET.status_code, "调用--查询属性--接口失败。")
        request_frame_work.response3(findThingEventUsingGET, "无法查询事件", "事件已被删除")

        print(
            "----------------------------------------------------------优模型----------------------------------------------------------")
        """修改优模型"""
        updateModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/updateProfile"
        updata_param2 = json.loads(create_param)
        updata_param2["description"] = new_description
        updateModelProfileByKeyUsingPOST = request_frame_work.request1(updateModelProfileByKeyUsingPOST_url, headers1,
                                                                       updata_param2, typed="post")
        request_frame_work.response1(updateModelProfileByKeyUsingPOST, "无法修改优模型", "调用修改优模型接口成功")

        """查询被修改的优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
        request_frame_work.response2(getModelProfileByKeyUsingGET, "查询优模型失败", "修改优模型失败", "优模型已被修改")

        """删除优模型"""
        deleteModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/delete"
        deleteModelProfileByKeyUsingPOST = request_frame_work.request1(deleteModelProfileByKeyUsingPOST_url, headers1,
                                                                       getmodel_param2, typed="post")
        request_frame_work.response1(deleteModelProfileByKeyUsingPOST, "删除优模型失败", "调用删除优模型接口成功")

        """查询被删除优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
        request_frame_work.response3(getModelProfileByKeyUsingGET, "查询优模型失败", "优模型已被删除")

    def tearDown(self) -> None:
        pass