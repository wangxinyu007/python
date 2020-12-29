# !/usr/bin/env python
# -*- coning: utf-8 -*-
# @Time     : 2018/10/23 14:28
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

        global description
        description = "修改之前"
        global updata_description
        updata_description = "修改之后"

        # 去除警告
        warnings.simplefilter("ignore", ResourceWarning)

        """获取登录的token"""
        global headers1
        headers1 = tokrn.get_token()

    @allure.story('新建优模型')
    def test_01(self):
        logs.info("----------------------------------------------test1------------------------------------------------")
        """进行查询优模型，有优模型进行删除。没有优模型不操作"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        # 进行序列化
        getmodel_param2 = json.loads(getmodel_param)
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                   getmodel_param2)
        if "utMsg" in getModelProfileByKeyUsingGET.json():
            logs.info("查询不到优模型，暂时不操作，结束if循环之后进行创建优模型")
        else:
            """查询到优模型，说明有优模型存在，进行删除优模型"""
            deleteModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/delete"
            delete_param2 = json.loads(getmodel_param)
            deleteModelProfileByKeyUsingPOST = request_frame_work.request1(deleteModelProfileByKeyUsingPOST_url,
                                                                           headers1, delete_param2, typed="post")
            self.assertEqual(200, deleteModelProfileByKeyUsingPOST.status_code, "调用--删除优模型--接口失败。")
            logs.info("查询到优模型，说明有优模型存在，进行删除优模型。")

        """创建优模型"""
        createModelProfileUsingPOST_url = jh_url + "/modelAdmin/createProfile"
        create_param1 = json.loads(create_param)
        createModelProfileUsingPOST = request_frame_work.request1(createModelProfileUsingPOST_url, headers1,
                                                                  create_param1, typed="post")
        # self.assertEqual(200, createModelProfileUsingPOST.status_code, "调用--进行创建优模型--接口失败。")
        request_frame_work.response1(createModelProfileUsingPOST, "无法创建优模型", "创建优模型成功")
        # if "utMsg" in createModelProfileUsingPOST.text:
        #     logs.error("无法创建优模型,错误状态码为: %s ,错误返回信息为：%s" % ((createModelProfileUsingPOST.status_code), createModelProfileUsingPOST.json()["utMsg"]))
        #     raise ValueError("无法创建优模型,错误状态码为: %s ,错误返回信息为：%s" % ((createModelProfileUsingPOST.status_code), createModelProfileUsingPOST.json()["utMsg"]))
        # else:
        #     logs.info("创建优模型成功")

        """新建属性"""
        createThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/create"
        create_Property_data2 = json.loads(create_Property_data)
        # create_Property_data2["modelId"] = "dasdadasdasdafasdf"
        create_Property_data2["modelId"] = createModelProfileUsingPOST.text
        createThingPropertyUsingPOST = request_frame_work.request1(createThingPropertyUsingPOST_url, headers1,
                                                                   create_Property_data2, typed="post")
        # self.assertEqual(200, createThingPropertyUsingPOST.status_code, "调用--进行创建优模型--接口失败。")
        request_frame_work.response1(createThingPropertyUsingPOST, "无法创建属性", "创建属性成功")
        # if "utMsg"  in createThingPropertyUsingPOST.text:
        #     logs.error("无法新建属性,状态码为: %s ,返回信息为：%s" % ((createThingPropertyUsingPOST.status_code),createThingPropertyUsingPOST.json()))
        #     raise ValueError("无法新建属性,状态码为: %s ,返回信息为：%s" % ((createThingPropertyUsingPOST.status_code),createThingPropertyUsingPOST.json()["utMsg"]))
        # else:
        #     logs.info("创建属性成功")

        """修改属性"""
        updateThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/update"
        updata_Property_data2 = json.loads(updata_Property_data)
        updata_Property_data2["id"] = createThingPropertyUsingPOST.text
        updateThingPropertyUsingPOST = request_frame_work.request1(updateThingPropertyUsingPOST_url, headers1,
                                                                   updata_Property_data2, typed="post")
        # self.assertEqual(200, updateThingPropertyUsingPOST.status_code, "调用--进行创建优模型--接口失败。")
        if "utMsg" in updateThingPropertyUsingPOST.text:
            logs.error("无法修改属性,状态码为: %s ,返回信息为：%s" % (
            (updateThingPropertyUsingPOST.status_code), updateThingPropertyUsingPOST.json()["utMsg"]))
            raise ValueError("无法修改属性,状态码为: %s ,返回信息为：%s" % (
            (updateThingPropertyUsingPOST.status_code), updateThingPropertyUsingPOST.json()["utMsg"]))
        else:
            logs.info("调用修改属性接口成功")

        """查询属性"""
        findThingPropertyUsingGET_url = jh_url + "/modelPropertyAdmin/find"
        findThingPropertyUsingGET_data = {"id": createThingPropertyUsingPOST.text}
        findThingPropertyUsingGET = request_frame_work.request1(findThingPropertyUsingGET_url, headers1,
                                                                findThingPropertyUsingGET_data)
        # self.assertEqual(200, findThingPropertyUsingGET.status_code, "调用--查询属性--接口失败。")
        if "utMsg" in findThingPropertyUsingGET.text:
            logs.error("无法查询属性,状态码为: %s ,返回信息为：%s" % (
            (findThingPropertyUsingGET.status_code), findThingPropertyUsingGET.json()["utMsg"]))
            raise ValueError("无法查询属性,状态码为: %s ,返回信息为：%s" % (
            (findThingPropertyUsingGET.status_code), findThingPropertyUsingGET.json()["utMsg"]))
        else:
            if "修改之后" != findThingPropertyUsingGET.json()["description"]:
                logs.error("修改属性失败,未修改成功，状态码为: %s ,返回信息为：%s" % (
                (findThingPropertyUsingGET.status_code), findThingPropertyUsingGET.json()["description"]))
                raise ValueError("修改属性失败,未修改成功，状态码为: %s ,返回信息为：%s" % (
                (findThingPropertyUsingGET.status_code), findThingPropertyUsingGET.json()["description"]))
            else:
                logs.info("属性已被修改")

        """删除属性"""
        deleteThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/delete"
        deleteThingPropertyUsingPOST_data = createThingPropertyUsingPOST.text
        deleteThingPropertyUsingPOST = requests.post(url=deleteThingPropertyUsingPOST_url, headers=headers1,
                                                     data=deleteThingPropertyUsingPOST_data)
        # self.assertEqual(200, deleteThingPropertyUsingPOST.status_code, "调用--删除属性--接口失败。状态码错误")
        if "utMsg" in deleteThingPropertyUsingPOST.text:
            logs.error("无法删除属性,状态码为: %s ,返回信息为：%s" % (
            (deleteThingPropertyUsingPOST.status_code), deleteThingPropertyUsingPOST.json()["utMsg"]))
            raise ValueError("无法删除属性,状态码为: %s ,返回信息为：%s" % (
            (deleteThingPropertyUsingPOST.status_code), deleteThingPropertyUsingPOST.json()["utMsg"]))
        else:
            logs.info("删除属性成功")

        """新建服务"""
        createThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/create"
        create_Service_data2 = json.loads(create_Service_data)
        create_Service_data2["modelId"] = createModelProfileUsingPOST.text
        createThingServiceUsingPOST = request_frame_work.request1(createThingServiceUsingPOST_url, headers1,
                                                                  create_Service_data2, typed="post")
        # self.assertEqual(200, createThingServiceUsingPOST.status_code, "调用  新建服务  接口失败。状态码错误")
        if "utMsg" in createThingServiceUsingPOST.text:
            logs.error("无法新建服务,状态码为: %s ,返回信息为：%s" % (
            (createThingServiceUsingPOST.status_code), createThingServiceUsingPOST.json()["utMsg"]))
            raise ValueError("调用--新建服务--接口失败,状态码为: %s ,返回信息为：%s" % (
            (createThingServiceUsingPOST.status_code), createThingServiceUsingPOST.json()["utMsg"]))
        else:
            logs.info("删除服务成功")

        """修改服务"""
        updateThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/update"
        updata_Service_data2 = json.loads(updata_Service_data)
        updata_Service_data2["id"] = createThingServiceUsingPOST.text
        updateThingServiceUsingPOST = request_frame_work.request1(updateThingServiceUsingPOST_url, headers1,
                                                                  updata_Service_data2, typed="post")
        # self.assertEqual(200, updateThingServiceUsingPOST.status_code, "调用  编辑服务  接口失败。状态码错误")
        if "utMsg" in updateThingServiceUsingPOST.text:
            logs.error("修改服务失败,状态码为: %s ,返回信息为：%s" % (
            (updateThingServiceUsingPOST.status_code), updateThingServiceUsingPOST.json()["utMsg"]))
            raise ValueError("调用--修改服务--接口失败,状态码为: %s ,返回信息为：%s" % (
            (updateThingServiceUsingPOST.status_code), updateThingServiceUsingPOST.json()["utMsg"]))
        else:
            logs.info("调用修改服务接口成功")
        """查询服务"""
        findThingServiceUsingGET_url = jh_url + "/modelServiceAdmin/find"
        findThingServiceUsingGET_data = {"id": createThingServiceUsingPOST.text}
        findThingServiceUsingGET = request_frame_work.request1(findThingServiceUsingGET_url, headers1,
                                                               findThingServiceUsingGET_data)
        # self.assertEqual(200, findThingServiceUsingGET.status_code, "调用  查询服务  接口失败。状态码错误")
        if "utMsg" in findThingServiceUsingGET.text:
            logs.error("无法查询服务,状态码为: %s ,返回信息为：%s" % (
            (findThingServiceUsingGET.status_code), findThingServiceUsingGET.json()["utMsg"]))
            raise ValueError("无法查询服务,状态码为: %s ,返回信息为：%s" % (
            (findThingServiceUsingGET.status_code), findThingServiceUsingGET.json()["utMsg"]))
        else:
            if "修改之后" != findThingServiceUsingGET.json()["description"]:
                logs.error("修改服务失败,未修改成功，状态码为: %s ,返回信息为：%s" % (
                (findThingPropertyUsingGET.status_code), findThingPropertyUsingGET.json()["utMsg"]))
                raise ValueError("修改服务失败,未修改成功，状态码为: %s ,返回信息为：%s" % (
                (findThingPropertyUsingGET.status_code), findThingPropertyUsingGET.json()["utMsg"]))
            else:
                logs.info("服务已被修改")

        """删除服务"""
        deleteThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/delete"
        deleteThingServiceUsingPOST_data = createThingServiceUsingPOST.text
        deleteThingServiceUsingPOST = requests.post(url=deleteThingServiceUsingPOST_url, headers=headers1,
                                                    data=deleteThingServiceUsingPOST_data)
        # self.assertEqual(200, deleteThingPropertyUsingPOST.status_code, "调用  删除属性  接口失败。状态码错误")
        if "utMsg" in deleteThingServiceUsingPOST.text:
            logs.error("删除服务失败,状态码为: %s ,返回信息为：%s" % (
            (deleteThingServiceUsingPOST.status_code), deleteThingServiceUsingPOST.json()["utMsg"]))
            raise ValueError("调用  删除服务  接口失败,状态码为: %s ,返回信息为：%s" % (
            (deleteThingServiceUsingPOST.status_code), deleteThingServiceUsingPOST.json()["utMsg"]))
        else:
            logs.info("删除服务成功")

        """新建事件"""
        createThingEventUsingPOST_url = jh_url + "/modelEventAdmin/create"
        create_Event_data2 = json.loads(create_Event_data)
        create_Event_data2["modelId"] = createModelProfileUsingPOST.text
        createThingEventUsingPOST = request_frame_work.request1(createThingEventUsingPOST_url, headers1,
                                                                create_Event_data2, typed="post")
        # self.assertEqual(200, createThingEventUsingPOST.status_code, "调用  新建事件  接口失败。状态码错误")
        if "utMsg" in createThingEventUsingPOST.text:
            logs.error("新建事件失败,状态码为: %s ,返回信息为：%s" % (
            (createThingEventUsingPOST.status_code), createThingEventUsingPOST.json()["utMsg"]))
            raise ValueError("调用  新建事件  接口失败,状态码为: %s ,返回信息为：%s" % (
            (createThingEventUsingPOST.status_code), createThingEventUsingPOST.json()["utMsg"]))
        else:
            logs.info("新建事件成功")
        """修改事件"""
        updateThingEventUsingPOST_url = jh_url + "/modelEventAdmin/update"
        updata_Event_data2 = json.loads(updata_Event_data)
        updata_Event_data2["id"] = createThingEventUsingPOST.text
        updateThingEventUsingPOST = request_frame_work.request1(updateThingEventUsingPOST_url, headers1,
                                                                updata_Event_data2, typed="post")
        # self.assertEqual(200, updateThingEventUsingPOST.status_code, "调用  编辑事件  接口失败。状态码错误")
        if "utMsg" in updateThingEventUsingPOST.text:
            logs.error("修改事件失败,状态码为: %s ,返回信息为：%s" % (
            (updateThingEventUsingPOST.status_code), updateThingEventUsingPOST.json()["utMsg"]))
            raise ValueError("调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % (
            (updateThingEventUsingPOST.status_code), updateThingEventUsingPOST.json()["utMsg"]))
        else:
            logs.info("调用修改事件接口成功")

        """查询事件"""
        findThingEventUsingGET_url = jh_url + "/modelEventAdmin/find"
        findThingEventUsingGET_data = {"id": createThingEventUsingPOST.text}
        findThingEventUsingGET = request_frame_work.request1(findThingEventUsingGET_url, headers1,
                                                             findThingEventUsingGET_data)
        # self.assertEqual(200, findThingEventUsingGET.status_code, "调用  查询事件  接口失败。状态码错误")
        if "utMsg" in findThingEventUsingGET.text:
            logs.error("查询事件失败,状态码为: %s ,返回信息为：%s" % (
            (findThingEventUsingGET.status_code), findThingEventUsingGET.json()["utMsg"]))
            raise ValueError("调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % (
            (findThingEventUsingGET.status_code), findThingEventUsingGET.json()["utMsg"]))
        else:
            if not "修改之后" == findThingEventUsingGET.json()["description"]:
                logs.error("修改事件失败,未修改成功，状态码为: %s ,返回信息为：%s" % (
                (findThingEventUsingGET.status_code), findThingEventUsingGET.json()["description"]))
                raise ValueError("修改事件失败,未修改成功，状态码为: %s ,返回信息为：%s" % (
                (findThingEventUsingGET.status_code), findThingEventUsingGET.json()["description"]))
            else:
                logs.info("事件已被修改")

        """删除事件"""
        deleteThingEventUsingPOST_url = jh_url + "/modelEventAdmin/delete"
        deleteThingEventUsingPOST_data = createThingEventUsingPOST.text
        deleteThingEventUsingPOST = requests.post(url=deleteThingEventUsingPOST_url, headers=headers1,
                                                  data=deleteThingEventUsingPOST_data)
        # self.assertEqual(200, deleteThingEventUsingPOST.status_code, "调用  删除属性  接口失败。状态码错误")
        if "utMsg" in deleteThingEventUsingPOST.text:
            logs.error("删除事件失败,状态码为: %s ,返回信息为：%s" % (
            (deleteThingEventUsingPOST.status_code), deleteThingEventUsingPOST.json()["utMsg"]))
            raise ValueError("调用  删除事件  接口失败,状态码为: %s ,返回信息为：%s" % (
            (deleteThingEventUsingPOST.status_code), deleteThingEventUsingPOST.json()["utMsg"]))
        else:
            logs.info("删除事件成功")

        """修改优模型"""
        updateModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/updateProfile"
        updata_param2 = json.loads(updata_param)
        updateModelProfileByKeyUsingPOST = request_frame_work.request1(updateModelProfileByKeyUsingPOST_url, headers1,
                                                                       updata_param2, typed="post")
        # self.assertEqual(200, updateModelProfileByKeyUsingPOST.status_code, "调用  编辑优模型  接口失败。状态码错误")
        if "utMsg" in updateModelProfileByKeyUsingPOST.text:
            logs.error("修改优模型失败,状态码为: %s ,返回信息为：%s" % (
            (updateModelProfileByKeyUsingPOST.status_code), updateModelProfileByKeyUsingPOST.json()["utMsg"]))
            raise ValueError("调用  修改优模型  接口失败,状态码为: %s ,返回信息为：%s" % (
            (updateModelProfileByKeyUsingPOST.status_code), updateModelProfileByKeyUsingPOST.json()["utMsg"]))
        else:
            logs.info("调用修改优模型接口成功")
        """查询被修改的优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                   getmodel_param2)
        if "utMsg" in getModelProfileByKeyUsingGET.text:
            logs.error("查询优模型失败,状态码为: %s ,返回信息为：%s" % (
            (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["utMsg"]))
            raise ValueError("调用  查询优模型  接口失败,状态码为: %s ,返回信息为：%s" % (
            (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["utMsg"]))
        else:
            if "修改之后" != getModelProfileByKeyUsingGET.json()["description"]:
                logs.error("修改优模型失败,状态码为: %s ,返回信息为：%s" % (
                (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["description"]))
                raise ValueError("修改优模型失败,状态码为: %s ,返回信息为：%s" % (
                (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["description"]))
            else:
                logs.info("优模型已被修改")

        """删除优模型"""
        deleteModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/delete"
        deleteModelProfileByKeyUsingPOST = request_frame_work.request1(deleteModelProfileByKeyUsingPOST_url, headers1,
                                                                       getmodel_param2, typed="post")
        if "utMsg" in deleteModelProfileByKeyUsingPOST.text:
            logs.error("删除优模型失败,状态码为: %s ,返回信息为：%s" % (
            (deleteModelProfileByKeyUsingPOST.status_code), deleteModelProfileByKeyUsingPOST.json()["utMsg"]))
            raise ValueError("调用   删除优模型接口  失败,状态码为: %s ,返回信息为：%s" % (
            (deleteModelProfileByKeyUsingPOST.status_code), deleteModelProfileByKeyUsingPOST.json()["utMsg"]))
        else:
            logs.info("调用删除优模型接口成功")

        """查询被删除优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                   getmodel_param2)
        if "utMsg" in getModelProfileByKeyUsingGET.text:
            logs.info("优模型已被删除")
        else:
            logs.error("查询优模型失败,状态码为: %s ,返回信息为：%s" % (
            (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["utMsg"]))
            raise ValueError("调用  查询优模型  接口失败,状态码为: %s ,返回信息为：%s" % (

                (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["utMsg"]))

    @allure.story('导入优模型')
    def test_02(self):
        logs.info("----------------------------------------------test2------------------------------------------------")
        """导入优模型 进行测试"""
        """进行查询优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "31"}
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                   getModelProfileByKeyUsingGET_param)
        """进行判断，如果没有报错信息。说明优模型存在，可以进行导入优模型进行修改，
                     如果有报错信息，说明没有优模型存在，进行创建优模型"""
        if "utMsg" not in getModelProfileByKeyUsingGET.json():
            """这里进行两次导入优模型进行修改。 防止第一次更改的，跟原有的优模型数据一样。 第二次再次进行修改，保证导入修改优模型接口正常"""
            """第一次导入优模型进行修改"""
            importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
            importSpecificationUsingPOST_param = {
                "profile": {"category": "ut-device", "description": description, "identifier": "112",
                            "name": description},
                "properties": [{"accessMode": "r",
                                "dataType": {"specs": {"min": -214648, "max": 2147483647, "step": 2}, "type": "int"},
                                "description": "修改属性之后", "identifier": "updata_Property_data", "name": "修改属性之后"}],
                "services": [
                    {"identifier": "service", "name": "服务更改之后", "inputData": [], "outputData": [], "callType": "async",
                     "requestMethod": "delete", "url": "exercitation Duis ex", "description": "修改服务之后"}],
                "events": [{"identifier": "device", "name": "修改事件之后", "type": "warning", "outputData": [],
                            "description": "修改事件之后", "topic": "sed aliqua"}]}
            importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,
                                                                       importSpecificationUsingPOST_param, typed="post")
            if "utMsg" in importSpecificationUsingPOST.text:
                raise ValueError("调用  第一次导入优模型进行修改接口  失败,状态码为: %s ,返回信息为：%s" % (
                (importSpecificationUsingPOST.status_code), importSpecificationUsingPOST.json()))

            """第一次进行查询"""
            getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
            getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "112"}
            getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                       getModelProfileByKeyUsingGET_param)
            if "utMsg" in getModelProfileByKeyUsingGET.text:
                raise ValueError("调用  第一次查询优模型  接口失败,状态码为: %s ,返回信息为：%s" % (
                (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
            else:
                if not "修改之前" == getModelProfileByKeyUsingGET.json()["description"]:
                    raise ValueError("第一次修改优模型失败，错误原因为 失败,状态码为: %s ,返回信息为：%s" % (
                    (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
                else:
                    pass

            """第二次通过导入优模型进行修改"""
            importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
            importSpecificationUsingPOST_param = {
                "profile": {"category": "ut-device", "description": updata_description, "identifier": "112",
                            "name": "更改之后"},
                "properties": [{"accessMode": "r",
                                "dataType": {"specs": {"min": -214648, "max": 2147483647, "step": 2}, "type": "int"},
                                "description": "修改属性之后", "identifier": "updata_Property_data", "name": "修改属性之后"}],
                "services": [
                    {"identifier": "service", "name": "服务更改之后", "inputData": [], "outputData": [], "callType": "async",
                     "requestMethod": "delete", "url": "exercitation Duis ex", "description": "修改服务之后"}],
                "events": [
                    {"identifier": "device", "name": "修改事件之后", "type": "warning", "outputData": [],
                     "description": "修改事件之后",
                     "topic": "sed aliqua"}]}
            importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,
                                                                       importSpecificationUsingPOST_param, typed="post")
            if "utMsg" in importSpecificationUsingPOST.text:
                raise ValueError("调用  第二次导入优模型进行修改接口  失败,状态码为: %s ,返回信息为：%s" % (
                    (importSpecificationUsingPOST.status_code), importSpecificationUsingPOST.json()))
            """导入优模型进行修改之后，进行查询"""
            getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
            getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "112"}
            getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                       getModelProfileByKeyUsingGET_param)
            if "utMsg" in getModelProfileByKeyUsingGET.text:
                raise ValueError("调用  第二次查询优模型  接口失败,状态码为: %s ,返回信息为：%s" % (
                (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
            else:
                if not "修改之后" == getModelProfileByKeyUsingGET.json()["description"]:
                    raise ValueError("第二次修改优模型失败，错误原因为 失败,状态码为: %s ,返回信息为：%s" % (
                    (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
                else:
                    pass
        else:
            """通过导入优模型进行创建优模型"""
            importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
            importSpecificationUsingPOST_param = {
                "profile": {"category": "ut-device", "description": description, "identifier": "112", "name": "更改之后"},
                "properties": [{"accessMode": "r",
                                "dataType": {"specs": {"min": -214648, "max": 2147483647, "step": 2}, "type": "int"},
                                "description": "修改属性之后", "identifier": "updata_Property_data", "name": "修改属性之后"}],
                "services": [
                    {"identifier": "service", "name": "服务更改之后", "inputData": [], "outputData": [], "callType": "async",
                     "requestMethod": "delete", "url": "exercitation Duis ex", "description": "修改服务之后"}],
                "events": [
                    {"identifier": "device", "name": "修改事件之后", "type": "warning", "outputData": [],
                     "description": "修改事件之后",
                     "topic": "sed aliqua"}]}
            importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,
                                                                       importSpecificationUsingPOST_param, typed="post")
            if "utMsg" in importSpecificationUsingPOST.text:
                raise ValueError("调用  导入优模型进行创建优模型  接口  失败,状态码为: %s ,返回信息为：%s" % (
                    (importSpecificationUsingPOST.status_code), importSpecificationUsingPOST.json()))
            """导入优模型进行修改之后，进行查询"""
            getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
            getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "112"}
            getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                       getModelProfileByKeyUsingGET_param)
            if "utMsg" in getModelProfileByKeyUsingGET.text:
                raise ValueError("调用  查询导入优模型进行创建优模型  接口失败,状态码为: %s ,返回信息为：%s" % (
                    (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
            else:
                if not "修改之前" == getModelProfileByKeyUsingGET.json()["description"]:
                    raise ValueError("导入优模型进行创建优模型，错误原因为 失败,状态码为: %s ,返回信息为：%s" % (
                        (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
                else:
                    pass

    def tearDown(self) -> None:
        pass