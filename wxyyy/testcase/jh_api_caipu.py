# !/usr/bin/env python
# -*- coning: utf-8 -*-
# @Time     : 2019/10/23 14:28
# @Author   : Mr.Gan
# Software  : PyCharm


import unittest
from frame_work import request_frame_work

from manage.getconfigparam import *


class MyTest(unittest.TestCase):
    param = {
        "key": "7468efb22ca0a3dd3b36eab3fb9b1e17",
        "menu": "青椒肉丝",
        "dtype": "",
        "pn": "",
        "rn": "2"
    }

    def setUp(self) -> None:
        pass

    def test_01(self):
        """传入正确的参数，验证返回接口是否正确"""
        url = jh_url + "/cook/query.php"
        response = request_frame_work.request(url, self.param, *(0, "请求成功"))


    def test_02(self):
        """验证接口请求次数不足时，反回的数据正不正确"""
        url = jh_url + "/cook/query.php"
        self.param["rn"] = "90"
        response = request_frame_work.request(url, self.param, *(10012, "当前可请求的次数不足"))

    def test_03(self):
        """验证接口请求次数不足时，反回的数据正不正确"""
        url = jh_url + "/cook/query.php"
        self.param["key"] = "lkadlkajdlkwadlkwajd;ljwad;l"
        response = request_frame_work.request(url, self.param, *(10012, "当前可请求的次数不足"))

    def tearDown(self) -> None:
        pass







# !/usr/bin/env python
# -*- coning: utf-8 -*-
# @Time     : 2019/10/23 14:28
# @Author   : Mr.Gan
# Software  : PyCharm


import unittest
from frame_work import request_frame_work
import requests

class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        url = "https://oauthuat.utcook.com/uaa/oauth/login"
        headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
                   "Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "username": "scf_adm",
            "password": "Ut123456",
            "grant_type": "password",
            "scope": "read"
        }
        response = requests.post(url=url, headers=headers, data=data)
        # print(response.text)
        access_token = response.json()["access_token"]
        Authorization_value = "bearer " + access_token
        headers1 = {
            "Content-Type": "application/json", "Authorization": Authorization_value
        }
        global headers1
    def test_01(self):
        """传入正确的参数，验证返回接口是否正确"""
        chaxun_url = "http://api.juheapi.com/japi/toh"
        chaxun_param = {"category":"ut-service","identifier":"3188221"}
        a=request_frame_work.request1(chaxun_url, headers1,chaxun_param)
        # response = requests.get(url=url, params=param)
        # self.assertEqual(response.status_code, 200)
        # text = response.json()
        # self.assertEqual(text.get("error_code"), 0) and self.assertEqual(text.get("reason"), "请求成功")
        # result = text.get("result")
        # for data in result:
        #     self.assertEqual(data.get("month"), param.get("month")) and self.assertEqual(data.get("day"), param.get("day"))
        #     self.assertIsNotNone(data.get("title")) and self.assertIsNotNone(data.get("_id"))
        #     self.assertIsNotNone(data.get("des"))

    # def test_02(self):
    #     """验证month 传入 13,  返回结果"""
    #     url1 = "https://mobileuat.utcook.com/utmodel/modelAdmin/findProfile"
    #     param1 = {"category": "ut-service", "identifier": "3188221"}
    #     request_frame_work.request("get", url1, param1, 205301, "错误的请求参数")
    #
    # def test_03(self):
    #     """验证day不传，返回结果"""
    #     url = "http://api.juheapi.com/japi/toh"
    #     param = {
    #         "key": "c6588d4c90620c51bc31978429bde010",
    #         "v": "1.0",
    #         "month": 13,
    #     }
    #     response = requests.get(url=url, params=param)
    #     self.assertEqual(response.status_code, 200)
    #     text = response.json()
    #     self.assertEqual(text.get("error_code"), 206301) and self.assertEqual(text.get("reason"), "错误的请求参数")
    #
    # def test_04(self):
    #     """传入错误的key，返回结果"""
    #     url = "http://api.juheapi.com/japi/toh"
    #     param = {
    #         "key": "c658^d4c90aaaa620c51bc31978429bde010",
    #         "v": "1.0",
    #         "month": 13,
    #     }
    #     response = requests.get(url=url, params=param)
    #     self.assertEqual(response.status_code, 200)
    #     text = response.json()
    #     self.assertEqual(text.get("error_code"), 10001) and self.assertEqual(text.get("reason"), "KEY ERROR!")

    def tearDown(self) -> None:
        pass