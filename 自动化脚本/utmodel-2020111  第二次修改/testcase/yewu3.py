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
        logs.info("----------------------------------------------test1------------------------------------------------")
        """进行查询优模型，有优模型进行删除。没有优模型不操作"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getmodel_param2 = json.loads(getmodel_param)
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
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
        createModelProfileUsingPOST = request_frame_work.request1(createModelProfileUsingPOST_url, headers1,create_param1, typed="post")
        self.assertEqual(200, createModelProfileUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", createModelProfileUsingPOST.text, "新建优模型失败")

        print("----------------------------------------------------------属性----------------------------------------------------------")
        """新建属性"""
        createThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/create"
        create_Property_data2 = json.loads(create_Property_data)
        create_Property_data2["modelId"] = createModelProfileUsingPOST.text
        # create_Property_data2["modelId"] = "qeqweqwe"
        createThingPropertyUsingPOST = request_frame_work.request1(createThingPropertyUsingPOST_url, headers1,create_Property_data2, typed="post")
        self.assertEqual(200, createThingPropertyUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg",createThingPropertyUsingPOST.text ,"新建属性失败")


        """修改属性"""
        updateThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/update"
        updata_Property_data2 = json.loads(updata_Property_data)
        updata_Property_data2["id"] = createThingPropertyUsingPOST.text
        updateThingPropertyUsingPOST = request_frame_work.request1(updateThingPropertyUsingPOST_url, headers1,
                                                                   updata_Property_data2, typed="post")
        self.assertEqual(200, updateThingPropertyUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", updateThingPropertyUsingPOST.text, "修改优模型失败")

        """查询属性"""
        findThingPropertyUsingGET_url = jh_url + "/modelPropertyAdmin/find"
        findThingPropertyUsingGET_data = {"id": createThingPropertyUsingPOST.text}
        findThingPropertyUsingGET = request_frame_work.request1(findThingPropertyUsingGET_url, headers1,
                                                                findThingPropertyUsingGET_data)
        self.assertEqual(200, findThingPropertyUsingGET.status_code, "状态码错误")
        self.assertEqual("修改之后", findThingPropertyUsingGET.json()["description"], "修改失败")

        """删除属性"""
        deleteThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/delete"
        deleteThingPropertyUsingPOST_data = createThingPropertyUsingPOST.text
        deleteThingPropertyUsingPOST = requests.post(url=deleteThingPropertyUsingPOST_url, headers=headers1,
                                                     data=deleteThingPropertyUsingPOST_data)
        self.assertEqual(200, deleteThingPropertyUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", deleteThingPropertyUsingPOST.text, "删除优模型失败")

        """查询被删除的属性"""
        findThingPropertyUsingGET_url = jh_url + "/modelPropertyAdmin/find"
        findThingPropertyUsingGET_data = {"id": createThingPropertyUsingPOST.text}
        findThingPropertyUsingGET = request_frame_work.request1(findThingPropertyUsingGET_url, headers1,
                                                                findThingPropertyUsingGET_data)
        self.assertEqual(409, findThingPropertyUsingGET.status_code, "状态码错误")
        self.assertIn("utMsg", findThingPropertyUsingGET.text, "未删除成功")

        print(
            "----------------------------------------------------------服务----------------------------------------------------------")
        """新建服务"""
        createThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/create"
        create_Service_data2 = json.loads(create_Service_data)
        create_Service_data2["modelId"] = createModelProfileUsingPOST.text
        createThingServiceUsingPOST = request_frame_work.request1(createThingServiceUsingPOST_url, headers1, create_Service_data2, typed="post")
        self.assertEqual(200, createThingServiceUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", createThingServiceUsingPOST.text, "新建服务失败")

        """修改服务"""
        updateThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/update"
        updata_Service_data2 = json.loads(updata_Service_data)
        updata_Service_data2["id"] = createThingServiceUsingPOST.text
        updateThingServiceUsingPOST = request_frame_work.request1(updateThingServiceUsingPOST_url, headers1,updata_Service_data2, typed="post")
        self.assertEqual(200, updateThingServiceUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", updateThingServiceUsingPOST.text, "修改服务失败")

        """查询服务"""
        findThingServiceUsingGET_url = jh_url + "/modelServiceAdmin/find"
        findThingServiceUsingGET_data = {"id": createThingServiceUsingPOST.text}
        findThingServiceUsingGET = request_frame_work.request1(findThingServiceUsingGET_url, headers1,
                                                               findThingServiceUsingGET_data)
        self.assertEqual(200, findThingServiceUsingGET.status_code, "状态码错误")
        self.assertEqual("修改之后", findThingServiceUsingGET.json()["description"], "修改失败")

        """删除服务"""
        deleteThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/delete"
        deleteThingServiceUsingPOST_data = createThingServiceUsingPOST.text
        deleteThingServiceUsingPOST = requests.post(url=deleteThingServiceUsingPOST_url, headers=headers1,
                                                    data=deleteThingServiceUsingPOST_data)
        self.assertEqual(200, deleteThingServiceUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", deleteThingServiceUsingPOST.text, "删除服务失败")

        """查询被删除的服务"""
        findThingServiceUsingGET_url = jh_url + "/modelServiceAdmin/find"
        findThingServiceUsingGET_data = {"id": createThingServiceUsingPOST.text}
        findThingServiceUsingGET = request_frame_work.request1(findThingServiceUsingGET_url, headers1,
                                                               findThingServiceUsingGET_data)
        self.assertEqual(409, findThingServiceUsingGET.status_code, "状态码错误")
        self.assertIn("utMsg", findThingServiceUsingGET.text, "未删除成功")

        print(
            "----------------------------------------------------------事件----------------------------------------------------------")
        """新建事件"""
        createThingEventUsingPOST_url = jh_url + "/modelEventAdmin/create"
        create_Event_data2 = json.loads(create_Event_data)
        create_Event_data2["modelId"] = createModelProfileUsingPOST.text
        createThingEventUsingPOST = request_frame_work.request1(createThingEventUsingPOST_url, headers1,
                                                                create_Event_data2, typed="post")
        self.assertEqual(200, createThingEventUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", createThingEventUsingPOST.text, "新建事件失败")

        """修改事件"""
        updateThingEventUsingPOST_url = jh_url + "/modelEventAdmin/update"
        updata_Event_data2 = json.loads(updata_Event_data)
        updata_Event_data2["id"] = createThingEventUsingPOST.text
        updateThingEventUsingPOST = request_frame_work.request1(updateThingEventUsingPOST_url, headers1,
                                                                updata_Event_data2, typed="post")
        self.assertEqual(200, updateThingEventUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", updateThingEventUsingPOST.text, "修改事件失败")

        """查询事件"""
        findThingEventUsingGET_url = jh_url + "/modelEventAdmin/find"
        findThingEventUsingGET_data = {"id": createThingEventUsingPOST.text}
        findThingEventUsingGET = request_frame_work.request1(findThingEventUsingGET_url, headers1,
                                                             findThingEventUsingGET_data)
        self.assertEqual(200, findThingEventUsingGET.status_code, "状态码错误")
        self.assertEqual("修改之后", findThingEventUsingGET.json()["description"], "修改失败")

        """删除事件"""
        deleteThingEventUsingPOST_url = jh_url + "/modelEventAdmin/delete"
        deleteThingEventUsingPOST_data = createThingEventUsingPOST.text
        deleteThingEventUsingPOST = requests.post(url=deleteThingEventUsingPOST_url, headers=headers1,
                                                  data=deleteThingEventUsingPOST_data)
        self.assertEqual(200, deleteThingEventUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", deleteThingEventUsingPOST.text, "删除服务失败")

        """查询被删除的事件"""
        findThingEventUsingGET_url = jh_url + "/modelEventAdmin/find"
        findThingEventUsingGET_data = {"id": createThingEventUsingPOST.text}
        findThingEventUsingGET = request_frame_work.request1(findThingEventUsingGET_url, headers1,
                                                             findThingEventUsingGET_data)
        self.assertEqual(409, findThingEventUsingGET.status_code, "状态码错误")
        self.assertIn("utMsg", findThingEventUsingGET.text, "未删除成功")

        print(
            "----------------------------------------------------------优模型----------------------------------------------------------")
        """修改优模型"""
        updateModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/updateProfile"
        updata_param2 = json.loads(updata_param)
        updateModelProfileByKeyUsingPOST = request_frame_work.request1(updateModelProfileByKeyUsingPOST_url, headers1,
                                                                       updata_param2, typed="post")
        self.assertEqual(200, updateModelProfileByKeyUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", updateModelProfileByKeyUsingPOST.text, "修改优模型失败")

        """查询被修改的优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                   getmodel_param2)
        self.assertEqual(200, getModelProfileByKeyUsingGET.status_code, "状态码错误")
        self.assertEqual("修改之后", getModelProfileByKeyUsingGET.json()["description"], "修改失败")

        """删除优模型"""
        deleteModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/delete"
        deleteModelProfileByKeyUsingPOST = request_frame_work.request1(deleteModelProfileByKeyUsingPOST_url, headers1,
                                                                       getmodel_param2, typed="post")
        self.assertEqual(200, deleteModelProfileByKeyUsingPOST.status_code, "状态码错误")
        self.assertNotIn("utMsg", deleteModelProfileByKeyUsingPOST.text, "删除优模型失败")

        """查询被删除优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                   getmodel_param2)
        self.assertEqual(409, getModelProfileByKeyUsingGET.status_code, "状态码错误")
        self.assertIn("utMsg", getModelProfileByKeyUsingGET.text, "未删除成功")

    @allure.story('导入优模型')
    def test_02(self):
        logs.info("----------------------------------------------test2------------------------------------------------")

        """进行查询优模型，有优模型进行删除。没有优模型不操作"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        # 进行序列化
        getmodel_param2 = json.loads(getmodel_param)
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
        print(getModelProfileByKeyUsingGET.text)
        if "utMsg" in getModelProfileByKeyUsingGET.json():
            logs.info("查询不到优模型，通过导入进行创建优模型")
            importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
            updata_import_param1 = json.loads(updata_import_param)
            importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1, updata_import_param1, typed="post")
            print(importSpecificationUsingPOST.text)
            # self.assertEqual(200, importSpecificationUsingPOST.status_code, "状态码错误")
            self.assertNotIn("utMsg", importSpecificationUsingPOST.text, "导入优模型失败")

            """导入优模型进行修改之后，进行查询"""
            getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
            print(getModelProfileByKeyUsingGET.text)
            # self.assertEqual(200, getModelProfileByKeyUsingGET.status_code, "状态码错误")
            self.assertEqual("修改之后", getModelProfileByKeyUsingGET.json()["description"], "修改失败")

        else:
            logs.info("查询到优模型，说明有优模型存在，导入优模型接口进行修改")
            importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
            updata_param2 = json.loads(updata_import_param)
            importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,updata_param2, typed="post")
            self.assertEqual(200, importSpecificationUsingPOST.status_code, "状态码错误")
            self.assertNotIn("utMsg", importSpecificationUsingPOST.text, "导入优模型失败")

            """通过导入优模型进行修改优模型之后，进行查询"""
            getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,
                                                                       getmodel_param2)
            self.assertEqual(200, getModelProfileByKeyUsingGET.status_code, "状态码错误")
            self.assertEqual("修改之后", getModelProfileByKeyUsingGET.json()["description"], "修改失败")

            importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
            updata_param2 = json.loads(updata_import_param)
            updata_param2["profile"]["description"] = old_description
            importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,updata_param2, typed="post")
            self.assertEqual(200, importSpecificationUsingPOST.status_code, "状态码错误")
            self.assertNotIn("utMsg", importSpecificationUsingPOST.text, "导入优模型失败")
            """通过导入优模型进行修改优模型之后，进行查询"""
            getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
            self.assertEqual(200, getModelProfileByKeyUsingGET.status_code, "状态码错误")
            self.assertEqual("修改之前", getModelProfileByKeyUsingGET.json()["description"], "修改失败")

    def tearDown(self) -> None:
        pass