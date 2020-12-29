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

    @allure.story('导入优模型进行创建')
    def test_01(self):
        """('导入优模型进行创建')"""
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
            deleteModelProfileByKeyUsingPOST = request_frame_work.request1(deleteModelProfileByKeyUsingPOST_url, headers1, delete_param2, typed="post")
            self.assertEqual(200, deleteModelProfileByKeyUsingPOST.status_code, "调用--删除优模型--接口失败。")
            logs.info("查询到优模型，说明有优模型存在，进行删除优模型。")

        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
        request_frame_work.response3(getModelProfileByKeyUsingGET, "删除优模型失败", "删除优模型成功")


        """通过导入接口进行创建优模型"""
        importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
        create_param1 = json.loads(import_param)
        importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,create_param1, typed="post")
        request_frame_work.response1(importSpecificationUsingPOST, "调用导入优模型接口失败", "调用导入优模型接口成功")

        """导入优模型进行创建之后，进行查询"""
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getmodel_param2)
        request_frame_work.response1(getModelProfileByKeyUsingGET, "通过导入进行创建优模型失败", "成功通过导入创建优模型")

    def tearDown(self) -> None:
        pass