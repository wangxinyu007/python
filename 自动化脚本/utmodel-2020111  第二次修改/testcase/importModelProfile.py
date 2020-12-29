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
        old_description = "更改之前"
        global new_description
        new_description = "更改之后"

        # 去除警告
        warnings.simplefilter("ignore", ResourceWarning)

        """获取登录的token"""
        global headers1
        headers1 = tokrn.get_token()

    @allure.story('导入优模型进行修改')
    def test_01(self):
        """'导入优模型进行修改')"""
        logs.info("----------------------------------------------test2------------------------------------------------")

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
        createModelProfileUsingPOST = request_frame_work.request1(createModelProfileUsingPOST_url, headers1,create_param1, typed="post")
        # self.assertEqual(200, createModelProfileUsingPOST.status_code, "调用--进行创建优模型--接口失败。")
        request_frame_work.response1(createModelProfileUsingPOST, "无法创建优模型", "创建优模型成功")

        logs.info("查询到优模型，说明有优模型存在，导入优模型接口进行修改")
        importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
        updata_param2=json.loads(updata_import_param)
        importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,updata_param2, typed="post")
        request_frame_work.response1(importSpecificationUsingPOST, "第一次调用导入优模型接口失败", "第一次调用导入优模型接口成功")

        """通过导入优模型进行修改优模型之后，进行查询"""
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
        request_frame_work.response2(getModelProfileByKeyUsingGET, "查询优模型失败", "第一次通过导入优模型修改优模型失败", "第一次修改优模型已被修改")

        importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
        updata_param2 = json.loads(import_param)
        importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,updata_param2, typed="post")
        request_frame_work.response1(importSpecificationUsingPOST, "第二次调用导入优模型接口失败", "第二次调用导入优模型接口成功")

        """通过导入优模型进行修改优模型之后，进行查询"""
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
        # request_frame_work.response2(getModelProfileByKeyUsingGET, "查询优模型失败", "第二次通过导入优模型修改优模型失败", "第二次修改优模型已被修改")
        if "utMsg" in getModelProfileByKeyUsingGET.text:
            logs.error("第二次查询优模型失败  :状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["utMsg"]))
            raise ValueError("第二次查询优模型失败  :状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["utMsg"]))
        else:
            if not "修改之前" == getModelProfileByKeyUsingGET.json()["description"]:
                logs.error("第二次通过导入优模型修改优模型失败  :状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["description"]))
                raise ValueError("第二次通过导入优模型修改优模型失败  :状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()["description"]))
            else:
                logs.info("第二次修改优模型已被修改")

    def tearDown(self) -> None:
        pass