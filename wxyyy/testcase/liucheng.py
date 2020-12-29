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
            "Content-Type": "application/json", "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJzY2ZfZGV2Iiwic2NvcGUiOlsicmVhZCJdLCJleHAiOjE2MTA4Nzc1NDYsImFjY291bnRTeXN0ZW1LZXkiOiJjb29rIiwiYXV0aG9yaXRpZXMiOlsicGxhdGZvcm1fYXBwX2FkZEFwcCIsInBsYXRmb3JtX2FjY291bnRfZ2V0QWxsVXNlcm5hbWVCeUF1dGhvcml0eSIsInBsYXRmb3JtX2FwcF9kZWxldGVNZW51IiwiZGV2ZWxvcGVyX3BsYXRmb3JtX2Jhc2ljX2luZm8iLCJwbGF0Zm9ybV9hcHBfY2hpbGRBY2NvdW50TWFuYWdlbWVudCIsInBsYXRmb3JtX2FwcF9jcmVhdGVDaGlsZEFjY291bnQiLCJwbGF0Zm9ybV91dG1vZGVsX2ZpbmRfcHJvcGVydHkiLCJwbGF0Zm9ybV9hcHBfbWFuYWdlbWVudCIsInBsYXRmb3JtX2FjY291bnRfY3JlYXRlQWNjb3VudFN5c3RlbSIsInBsYXRmb3JtX3V0bW9kZWxfZmluZF9wcm9maWxlIiwiZGV2ZWxvcGVyX3BsYXRmb3JtX3NlY3VyaXR5X3NldHRpbmciLCJkZXZlbG9wZXJfYWNjb3VudF9zeXN0ZW1fbGlzdCIsInBsYXRmb3JtX3V0bW9kZWxfbGlzdF9wcm9maWxlIiwicGxhdGZvcm1fYXBwX2JpbmRBdXRoMlVzZXIiLCJwbGF0Zm9ybV91dG1vZGVsX3Byb3BlcnR5bWFuYWdlciIsImZ1bmN0aW9uX2Rldl9xdWVyeSIsInBsYXRmb3JtX2FwcF9nZXRBcHAiLCJwbGF0Zm9ybV9hcHBfYmluZEF1dGhHcm91cDJVc2VyIiwicGxhdGZvcm1fYXBwX2VtcG93ZXJNYW5hZ2VtZW50IiwicGxhdGZvcm1fYXBwX2F1dGhvcml0eU1hbmFnZW1lbnQiLCJwbGF0Zm9ybV9hY2NvdW50X3VwZGF0ZUFjY291bnRTeXN0ZW1TdGF0dXMiLCJwbGF0Zm9ybV91dG1vZGVsX3VwZGF0ZV9wcm9wZXJ0eSIsInBsYXRmb3JtX3V0bW9kZWxfcXVlcnlfcHJvcGVydHkiLCJwbGF0Zm9ybV91dG1vZGVsX2V2ZW50bWFuYWdlciIsInBsYXRmb3JtX3V0bW9kZWxfaW1wb3J0X3Byb2ZpbGUiLCJkZXZlbG9wZXJfcGxhdGZvcm1fY2hhcmFjdG9yX21hbmFnZW1lbnQiLCJwbGF0Zm9ybV91dG1vZGVsX3Byb2ZpbGVtYW5hZ2VyIiwicGxhdGZvcm1fdXRtb2RlbF9maW5kX2V2ZW50IiwicGxhdGZvcm1fYXBwX2FkZEF1dGhvcml0eUdyb3VwIiwicGxhdGZvcm1fYXBwX2FsbEFwcHMiLCJwbGF0Zm9ybV91dG1vZGVsX3VwZGF0ZV9zZXJ2aWNlIiwiZnVuY3Rpb25fZGV2X2dldENvZGUiLCJwbGF0Zm9ybV9hY2NvdW50X3F1ZXJ5VXNlckJ5QXV0aEdyb3VwIiwicGxhdGZvcm1fYXBwX21lbnVNYW5hZ2VtZW50IiwiZnVuY3Rpb25fZGV2X2xpc3QiLCJwbGF0Zm9ybV9hcHBfYWxsQXV0aG9yaXRpZXMiLCJwbGF0Zm9ybV91dG1vZGVsX2NyZWF0ZV9zZXJ2aWNlIiwicGxhdGZvcm1fdXNlcl9iYXRjaFJlZ2lzdGVyIiwicGxhdGZvcm1fdXRtb2RlbF91cGRhdGVfcHJvZmlsZSIsImZ1bmN0aW9uX2Rldl9saXN0QWxsIiwiZnVuY3Rpb25fZGV2ZWxvcGVyIiwicGxhdGZvcm1fYXBwX2JpbmRBdXRoMkF1dGhHcm91cCIsImRldmVsb3Blcl9wbGF0Zm9ybV9hY2NvdW50X2JpbmQiLCJmdW5jdGlvbl9kZXZfZGVsZXRlIiwicGxhdGZvcm1fdXRtb2RlbF91cGRhdGVfZXZlbnQiLCJwbGF0Zm9ybV91dG1vZGVsX3NldF9wcm9maWxlX3RhZ3MiLCJwbGF0Zm9ybV9hY2NvdW50X2dldEFsbFVzZXJuYW1lQnlBdXRob3JpdHlHcm91cCIsImZ1bmN0aW9uX2Rldl9jcmVhdGUiLCJwbGF0Zm9ybV9hcHBfYmluZEF1dGhHcm91cDJNZW51IiwicGxhdGZvcm1fYXBwX3BhZ2VBbGxBdXRob3JpdGllcyIsImRldmVsb3Blcl9wbGF0Zm9ybV9hdXRob3JpdHlfbWFuYWdlbWVudCIsInBsYXRmb3JtX2FjY291bnRfcGFnZUFjY291bnRTeXN0ZW1Vc2VycyIsInBsYXRmb3JtX3V0bW9kZWxfbGlzdF9wcm9maWxlX2J5X2tleSIsInBsYXRmb3JtX3V0bW9kZWxfZGV2ZWxvcGVyIiwicGxhdGZvcm1fdXRtb2RlbF9kZWxldGVfcHJvZmlsZSIsInBsYXRmb3JtX3V0bW9kZWxfY3JlYXRlX3Byb2ZpbGUiLCJjbG91ZGV4ZWN1dGVfcHVibGlzaF9kZXZlbG9wZXIiLCJwbGF0Zm9ybV9hcHBfY2hpbGRVc2VycyIsInBsYXRmb3JtX3V0bW9kZWxfZGVsZXRlX2V2ZW50IiwicGxhdGZvcm1fdXNlcl9saXN0TnVtYmVyIiwiY2xvdWRleGVjdXRlX3Jldm9rZV9zZXJ2aWNlIiwicGxhdGZvcm1fdXRtb2RlbF9zZXJ2aWNlbWFuYWdlciIsInBsYXRmb3JtX2FwcF9nZXRNZW51IiwicGxhdGZvcm1fdXRtb2RlbF9saXN0X3Byb3BlcnR5IiwiY3VzdG9tZmxvd19kZXZlbG9wZXIiLCJwbGF0Zm9ybV91dG1vZGVsX2NyZWF0ZV9wcm9wZXJ0eSIsInBsYXRmb3JtX2FwcF91cGRhdGVBcHAiLCJwbGF0Zm9ybV9hcHBfYWxsQXV0aG9yaXR5R3JvdXBzIiwicGxhdGZvcm1fYXBwX2JpbmRBdXRoMk1lbnUiLCJwbGF0Zm9ybV9hcHBfZGVsZXRlQXV0aG9yaXR5R3JvdXAiLCJwbGF0Zm9ybV9hcHBfdW5CaW5kQXV0aDJBdXRoR3JvdXAiLCJwbGF0Zm9ybV91dG1vZGVsX3F1ZXJ5X3Byb2ZpbGUiLCJwbGF0Zm9ybV9hcHBfYWRkQXV0aG9yaXR5IiwicGxhdGZvcm1fYXBwX3VwZGF0ZUF1dGhvcml0eUdyb3VwIiwicGxhdGZvcm1fZGV2ZWxvcGVyIiwiZGV2ZWxvcGVyX3BsYXRmb3JtX21lbnVfbWFuYWdlbWVudCIsInBsYXRmb3JtX2FjY291bnRfY3JlYXRVc2VyVW5kZXJBY2NvdW50IiwicGxhdGZvcm1fdXRtb2RlbF9xdWVyeV9zZXJ2aWNlIiwicGxhdGZvcm1fdXRtb2RlbF9leHBvcnRfcHJvZmlsZSIsInBsYXRmb3JtX2FwcF9kZWxldGVBdXRob3JpdHkiLCJwbGF0Zm9ybV9hY2NvdW50X3VwZGF0ZVVzZXJTdGF0dXMiLCJwbGF0Zm9ybV9hcHBfYWRkTWVudSIsImRldmVsb3Blcl9wbGF0Zm9ybV9hcHBfbGlzdCIsInBsYXRmb3JtX3V0bW9kZWxfZmluZF9zZXJ2aWNlIiwicGxhdGZvcm1fdXRtb2RlbF9saXN0X3NlcnZpY2UiLCJwbGF0Zm9ybV9hY2NvdW50X3BhZ2VBY2NvdW50U3lzdGVtcyIsImRldmVsb3Blcl9wbGF0Zm9ybV9zdWJfYWNjb3VudF9tYW5hZ2VtZW50IiwicGxhdGZvcm1fYXBwX2FsbE1lbnVzIiwicGxhdGZvcm1fdXRtb2RlbF9saXN0X2V2ZW50IiwiZGV2ZWxvcGVyX3BsYXRmb3JtX2RldmVsb3BlciIsImRldmVsb3Blcl9zZXJ2aWNlX2RldiIsInBsYXRmb3JtX2FwcF9hcHBMaXN0IiwiZGV2ZWxvcGVyX3NlcnZpY2VfY3VzdG9taXphdGlvbl9ob21lIiwicGxhdGZvcm1fYWNjb3VudF91cGRhdGVBY2NvdW50U3lzdGVtIiwicGxhdGZvcm1fdXRtb2RlbF9kZWxldGVfcHJvcGVydHkiLCJwbGF0Zm9ybV91dG1vZGVsX2NyZWF0ZV9ldmVudCIsImRldmVsb3Blcl9wbGF0Zm9ybV9mdW5jdGlvbl9tYW5hZ2VtZW50IiwicGxhdGZvcm1fYXBwX3VwZGF0ZUF1dGhvcml0eSIsInBsYXRmb3JtX3V0bW9kZWxfZGVsZXRlX3NlcnZpY2UiLCJwbGF0Zm9ybV9hcHBfdW5CaW5kQXV0aDJNZW51IiwicGxhdGZvcm1fdXRtb2RlbF9xdWVyeV9ldmVudCIsInBsYXRmb3JtX2FwcF9hdXRob3JpdHlHcm91cE1hbmFnZW1lbnQiLCJwbGF0Zm9ybV9hcHBfY2hhbmdlQXBwU3RhdHVzIiwicGxhdGZvcm1fYXBwX3VuQmluZEF1dGhHcm91cDJNZW51IiwicGxhdGZvcm1fYXBwX3VwZGF0ZU1lbnUiXSwianRpIjoiNWVjOTZhOTEtYjJjZi00ZWRjLTg5MjQtNDYzYjdiMDdhMTFlIiwiY2xpZW50X2lkIjoic3NvLWdhdGV3YXkiLCJ1c2VybmFtZSI6InNjZl9kZXYifQ.bFP2EiKrXFDEN7edkVoL8qpDx1luDdjAoyn53iWKlbI"
        }
        """进行查询优模型"""
        print(headers1)
        j = "https://mobileuat.utcook.com/utmodel/modelDeveloper/createProfile"
        print(j)
        print(type(j))
        l = {"category":"flow-service","description":"do","identifier":"90","name":"09"}
        print(l)
        print(type(l))
        g = requests.post(j, headers1, json=l)
        print(g.text)
        print("--------------------------------------------------------------------------")
        create_url = jh_url + "/modelDeveloper/createProfile"
        print(create_url)
        print(type(create_url))
        create_param1 = json.loads(create_param)
        print(create_param1)
        print(type(create_param1))
        create = request_frame_work.request1(create_url, headers1, create_param1, typed="post")
        print(create.text)







    def test_01(self):
        """进行判断，如果没有报错信息。说明优模型存在，进行删除优模型，
                     如果有报错信息，说明没有优模型存在，进行创建优模型"""
        # if "utMsg" not in chaxun.json():
        #     """删除优模型"""
        #     delete_url = jh_url + "/modelAdmin/delete"
        #     chaxun_param2 = json.loads(chaxun_param)
        #     delete = request_frame_work.request1(delete_url, headers1, chaxun_param2,typed="post")
        #     self.assertEqual(200, delete.status_code, "调用  删除优模型  接口失败。状态码错误")
        #     if "utMsg"  in delete.text:
        #         raise ValueError("调用   删除优模型接口  失败,状态码为: %s ,返回信息为：%s" % ((delete.status_code), delete.json()))

        # """创建优模型"""
        # create_url=jh_url +"/modelDeveloper/createProfile"
        # create_param1 = json.loads(create_param)
        # create=request_frame_work.request1(create_url, headers1, create_param1,typed="post")
        # print(create.text)


        # j="https://mobileuat.utcook.com/utmodel/modelDeveloper/createProfile"
        # l={"category":"flow-service","description":"do","identifier":"90","name":"09"}
        # g=requests.post(j,headers1,json=l)
        # print(g.text)
        # self.assertEqual(200, create.status_code, "调用  进行创建优模型  接口失败。状态码错误")

        # def create_updata_check_delete_check(create_Property_url,create_Property_data,updata_Property_url,updata_Property_data,chaxun_Property_url,delete_Property_url):
        #     """新建属性"""
        #     create_Property_data2 = json.loads(create_Property_data)
        #     create_Property_data2["modelId"] = create.text
        #     Property = request_frame_work.request1(create_Property_url, headers1, create_Property_data2, typed="post")
        #     if "utMsg" in Property.text:
        #         if "属性更改之前" == create_Property_data2["description"]:
        #             raise ValueError("调用  新建属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Property.status_code), Property.json()))
        #         if "服务更改之前" == create_Property_data2["description"]:
        #             raise ValueError("调用  新建服务  接口失败,状态码为: %s ,返回信息为：%s" % ((Property.status_code), Property.json()))
        #         if "事件更改之前" == create_Property_data2["description"]:
        #             raise ValueError("调用  新建事件  接口失败,状态码为: %s ,返回信息为：%s" % ((Property.status_code), Property.json()))
        #
        #     """编辑属性"""
        #     updata_Property_data2 = json.loads(updata_Property_data)
        #     updata_Property_data2["id"] = Property.text
        #     # updata_Property_data2["id"] = Property.text
        #     Updata_Property = request_frame_work.request1(updata_Property_url, headers1, updata_Property_data2,typed="post")
        #     if "utMsg" in Updata_Property.text:
        #         if "属性更改之前" == create_Property_data2["description"]:
        #             raise ValueError("调用  编辑属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Property.status_code), Updata_Property.json()))
        #         if "服务更改之前" == create_Property_data2["description"]:
        #             raise ValueError("调用  编辑服务  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Property.status_code), Updata_Property.json()))
        #         if "事件更改之前" == create_Property_data2["description"]:
        #             raise ValueError("调用  编辑事件  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Property.status_code), Updata_Property.json()))
        #
        #     """查询属性"""
        #     Property_data = {"id": Property.text}
        #     chaxun_Property = request_frame_work.request1(chaxun_Property_url, headers1, Property_data)
        #     name=list(updata_Property_data2)[0]
        #     if "utMsg" in chaxun_Property.json():
        #         if "修改属性之后" == updata_Property_data2[name]["description"]:
        #             raise ValueError("调用  删除属性  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Property.status_code), chaxun_Property.json()))
        #         if "修改服务之后" == updata_Property_data2[name]["description"]:
        #             raise ValueError("调用  删除服务  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Property.status_code), chaxun_Property.json()))
        #         if "修改事件之后" == updata_Property_data2[name]["description"]:
        #             raise ValueError("调用  删除事件  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Property.status_code), chaxun_Property.json()))
        #     elif "name" in chaxun_Property.json():
        #         if "修改属性之后" == chaxun_Property.json()["description"]:
        #             if "修改属性之后" != chaxun_Property.json()["name"]:
        #                 raise ValueError("修改属性失败，错误原因为 : %s " % (chaxun_Property.json()))
        #         if "修改服务之后" == chaxun_Property.json()["description"]:
        #             if not "修改服务之后1" == chaxun_Property.json()["name"]:
        #                 raise ValueError("修改服务失败，错误原因为 : %s " % (chaxun_Property.json()))
        #         if "修改事件之后" == chaxun_Property.json()["description"]:
        #             if not "修改事件之后" == chaxun_Property.json()["name"]:
        #                 raise ValueError("修改事件失败，错误原因为 : %s " % (chaxun_Property.json()))
        #
        #     """删除属性"""
        #     delete_Property_data = Property.text
        #     Delete_Property = requests.post(url=delete_Property_url, headers=headers1, data=delete_Property_data)
        #     name = list(updata_Property_data2)[0]
        #     if "utMsg" in Delete_Property.text:
        #         if "修改属性之后" == updata_Property_data2[name]["description"]:
        #             raise ValueError("调用  删除属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Delete_Property.status_code), Delete_Property.json()))
        #         if "修改服务之后" == updata_Property_data2[name]["description"]:
        #             raise ValueError("调用  删除服务  接口失败,状态码为: %s ,返回信息为：%s" % ((Delete_Property.status_code), Delete_Property.json()))
        #         if "修改事件之后" == updata_Property_data2[name]["description"]:
        #             raise ValueError("调用  删除事件  接口失败,状态码为: %s ,返回信息为：%s" % ((Delete_Property.status_code), Delete_Property.json()))
        #
        #     """查询属性"""
        #     Property_delete_data = {"id": Property.text}
        #     chaxun_delete_Property = request_frame_work.request1(chaxun_Property_url, headers1,Property_delete_data)
        #     name = list(updata_Property_data2)[0]
        #     if not "utMsg" in chaxun_delete_Property.json():
        #         if "修改属性之后" == updata_Property_data2[name]["description"]:
        #             raise ValueError("调用  查询属性  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_delete_Property.status_code), chaxun_delete_Property.json()))
        #         if "修改服务之后" == updata_Property_data2[name]["description"]:
        #             raise ValueError("调用  查询服务  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_delete_Property.status_code), chaxun_delete_Property.json()))
        #         if "修改事件之后" == updata_Property_data2[name]["description"]:
        #             raise ValueError("调用  查询事件  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_delete_Property.status_code), chaxun_delete_Property.json()))
        #     elif "name" in chaxun_delete_Property.json():
        #         if "修改属性之后" == chaxun_Property.json()["description"]:
        #             if not "修改属性之后" == chaxun_Property.json()["name"]:
        #                 raise ValueError("修改属性失败，错误原因为 : %s " % (chaxun_Property.json()))
        #         if "修改服务之后" == chaxun_Property.json()["description"]:
        #             if not "修改服务之后" == chaxun_Property.json()["name"]:
        #                 raise ValueError("修改服务失败，错误原因为 : %s " % (chaxun_Property.json()))
        #         if "修改事件之后" == chaxun_Property.json()["description"]:
        #             if not "修改事件之后" == chaxun_Property.json()["name"]:
        #                 raise ValueError("修改事件失败，错误原因为 : %s " % (chaxun_Property.json()))
        #
        #
        # """新建属性-编辑-查询-删除-查询流程"""
        # create_Property_url = jh_url + "/modelPropertyAdmin/create"
        # updata_Property_url = jh_url + "/modelPropertyAdmin/update"
        # chaxun_Property_url = jh_url + "/modelPropertyAdmin/find"
        # delete_Property_url = jh_url + "/modelPropertyAdmin/delete"
        # create_updata_check_delete_check(create_Property_url,create_Property_data,updata_Property_url,updata_Property_data,chaxun_Property_url,delete_Property_url)
        # """新建服务-编辑-查询-删除-查询流程"""
        # create_Service_url = jh_url + "/modelServiceAdmin/create"
        # updata_Service_url = jh_url + "/modelServiceAdmin/update"
        # chaxun_Service_url = jh_url + "/modelServiceAdmin/find"
        # delete_Service_url = jh_url + "/modelServiceAdmin/delete"
        # create_updata_check_delete_check(create_Service_url, create_Service_data, updata_Service_url,updata_Service_data, chaxun_Service_url, delete_Service_url)
        # """新建事件-编辑-查询-删除-查询流程"""
        # create_Event_url = jh_url + "/modelEventAdmin/create"
        # updata_Event_url = jh_url + "/modelEventAdmin/update"
        # chaxun_Event_url = jh_url + "/modelEventAdmin/find"
        # delete_Event_url = jh_url + "/modelEventAdmin/delete"
        # create_updata_check_delete_check(create_Event_url, create_Event_data, updata_Event_url,updata_Event_data, chaxun_Event_url, delete_Event_url)
        #
        # """编辑优模型"""
        # updata_url = jh_url + "/modelAdmin/updateProfile"
        # updata_param2 = json.loads(updata_param)
        # # updata_param2["id"] = Event.text
        # Updata_model = request_frame_work.request1(updata_url, headers1, updata_param2, typed="post")
        # self.assertEqual(200, Updata_model.status_code, "调用  编辑优模型  接口失败。状态码错误")
        # if "utMsg" in Updata_model.text:
        #     raise ValueError(
        #         "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_model.status_code), Updata_model.json()))
        #
        # """查询被修改的优模型"""
        # chaxun_updata_model_url = jh_url + "/modelAdmin/findProfile"
        # chaxun_updata_model_param12 = json.loads(chaxun_param)
        # chaxun_updata_model = request_frame_work.request1(chaxun_updata_model_url, headers1, chaxun_updata_model_param12)
        # self.assertEqual(200, chaxun_updata_model.status_code, "调用  查询被修改的优模型  接口失败。状态码错误")
        # if "utMsg" in chaxun_updata_model.text:
        #     raise ValueError(
        #         "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_updata_model.status_code), chaxun_updata_model.json()))
        # elif "name" in chaxun.text:
        #     if not "修改之后" == chaxun_updata_model.json()["description"]:
        #         raise ValueError("修改优模型失败，错误原因为 : %s " % (chaxun_updata_model.json()))
        #
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
        #
        #
        #
        #
        #









        # """新建属性"""
        # create_Property_url=jh_url +"/modelPropertyAdmin/create"
        # create_Property_data2=json.loads(create_Property_data)
        # create_Property_data2["modelId"]=create.text
        # Property= request_frame_work.request1(create_Property_url, headers1, create_Property_data2, typed="post")
        # self.assertEqual(200, Property.status_code, "调用  新建属性  接口失败。状态码错误")
        # if "utMsg"  in Property.text:
        #     raise ValueError("调用  新建属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Property.status_code), Property.json()))
        #
        # """新建服务"""
        # create_Service_url = jh_url + "/modelServiceAdmin/create"
        # create_Service_data2 = json.loads(create_Service_data)
        # create_Service_data2["modelId"] = create.text
        # Service = request_frame_work.request1(create_Service_url, headers1, create_Service_data2, typed="post")
        # self.assertEqual(200, Service.status_code, "调用  新建服务  接口失败。状态码错误")
        # if "utMsg"  in Service.text:
        #     raise ValueError("调用  新建属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Service.status_code), Service.json()))
        #
        # """新建事件"""
        # create_Event_url = jh_url + "/modelEventAdmin/create"
        # create_Event_data2 = json.loads(create_Event_data)
        # create_Event_data2["modelId"] = create.text
        # Event = request_frame_work.request1(create_Event_url, headers1, create_Event_data2, typed="post")
        # self.assertEqual(200, Event.status_code, "调用  新建事件  接口失败。状态码错误")
        # if "utMsg"  in Event.text:
        #     raise ValueError("调用  新建属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Event.status_code), Event.json()))
        #
        # """编辑属性"""
        # updata_Property_url = jh_url + "/modelPropertyAdmin/update"
        # updata_Property_data2 = json.loads(updata_Property_data)
        # updata_Property_data2["id"] = Property.text
        # Updata_Property = request_frame_work.request1(updata_Property_url, headers1, updata_Property_data2,typed="post")
        # self.assertEqual(200, Updata_Property.status_code, "调用  编辑属性  接口失败。状态码错误")
        # if "utMsg"  in Updata_Property.text:
        #     raise ValueError("调用  修改属性  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Property.status_code), Updata_Property.json()))
        #
        # """查询属性"""
        # chaxun_Property_url=jh_url+ "/modelPropertyAdmin/find"
        # Property_data={"id":Property.text}
        # chaxun_Property= request_frame_work.request1(chaxun_Property_url, headers1, Property_data)
        # self.assertEqual(200, chaxun_Property.status_code, "调用  查询属性  接口失败。状态码错误")
        # if "utMsg"  in chaxun_Property.text:
        #     raise ValueError("调用  修改属性  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Property.status_code), chaxun_Property.json()))
        # elif "name"  in chaxun_Property.text:
        #     if not "修改属性之后" == chaxun_Property.json()["name"]:
        #         raise ValueError("修改属性失败，错误原因为 : %s " % (chaxun_Property.json()))
        #
        # """删除属性"""
        # delete_Property_url=jh_url+ "/modelPropertyAdmin/delete"
        # delete_Property_data = Property.text
        # Delete_Property = requests.post(url=delete_Property_url, headers=headers1, data=delete_Property_data)
        # self.assertEqual(200, Delete_Property.status_code, "调用  删除属性  接口失败。状态码错误")
        # if "utMsg" in Delete_Property.text:
        #     raise ValueError("调用  删除属性接口   失败的原因为 【{}】".format(Delete_Property.json()["utMsg"]))
        #
        # """编辑服务"""
        # updata_Service_url = jh_url + "/modelServiceAdmin/update"
        # updata_Service_data2 = json.loads(updata_Service_data)
        # updata_Service_data2["id"] = Service.text
        # Updata_Service = request_frame_work.request1(updata_Service_url, headers1, updata_Service_data2,typed="post")
        # self.assertEqual(200, Updata_Service.status_code, "调用  编辑服务  接口失败。状态码错误")
        # if "utMsg" in Updata_Service.text:
        #     raise ValueError(
        #         "调用  修改服务  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Service.status_code), Updata_Service.json()))
        #
        # """查询服务"""
        # chaxun_Service_url = jh_url + "/modelServiceAdmin/find"
        # Service_data = {"id": Service.text}
        # chaxun_Service = request_frame_work.request1(chaxun_Service_url, headers1, Service_data)
        # self.assertEqual(200, chaxun_Service.status_code, "调用  查询服务  接口失败。状态码错误")
        # if "utMsg" in chaxun_Service.text:
        #     raise ValueError(
        #         "调用  修改服务  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Service.status_code), chaxun_Service.json()))
        # elif "name" in chaxun_Service.text:
        #     if not "修改服务之后" == chaxun_Service.json()["name"]:
        #         raise ValueError("修改服务失败，错误原因为 : %s " % (chaxun_Service.json()))
        #
        # """编辑事件"""
        # updata_Event_url = jh_url + "/modelEventAdmin/update"
        # updata_Event_data2 = json.loads(updata_Event_data)
        # updata_Event_data2["id"] = Event.text
        # Updata_Event = request_frame_work.request1(updata_Event_url, headers1, updata_Event_data2,typed="post")
        # self.assertEqual(200, Updata_Event.status_code, "调用  编辑事件  接口失败。状态码错误")
        # if "utMsg" in Updata_Event.text:
        #     raise ValueError(
        #         "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_Event.status_code), Updata_Event.json()))
        #
        # """查询事件"""
        # chaxun_Event_url = jh_url + "/modelEventAdmin/find"
        # Event_data = {"id": Event.text}
        # chaxun_Event = request_frame_work.request1(chaxun_Event_url, headers1, Event_data)
        # self.assertEqual(200, chaxun_Event.status_code, "调用  查询事件  接口失败。状态码错误")
        # if "utMsg" in chaxun_Event.text:
        #     raise ValueError(
        #         "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_Event.status_code), chaxun_Event.json()))
        # elif "name" in chaxun_Event.text:
        #     if not "修改事件之后" == chaxun_Event.json()["name"]:
        #         raise ValueError("修改事件失败，错误原因为 : %s " % (chaxun_Event.json()))
        #
        # """编辑优模型"""
        # updata_url = jh_url + "/modelAdmin/updateProfile"
        # updata_param2 = json.loads(updata_param)
        # # updata_param2["id"] = Event.text
        # Updata_model = request_frame_work.request1(updata_url, headers1, updata_param2, typed="post")
        # self.assertEqual(200, Updata_model.status_code, "调用  编辑优模型  接口失败。状态码错误")
        # if "utMsg" in Updata_model.text:
        #     raise ValueError(
        #         "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((Updata_model.status_code), Updata_model.json()))
        #
        # """查询被修改的优模型"""
        # chaxun_updata_model_url = jh_url + "/modelAdmin/findProfile"
        # chaxun_updata_model_param12 = json.loads(chaxun_param)
        # chaxun_updata_model = request_frame_work.request1(chaxun_updata_model_url, headers1, chaxun_updata_model_param12)
        # self.assertEqual(200, chaxun_updata_model.status_code, "调用  查询被修改的优模型  接口失败。状态码错误")
        # if "utMsg" in chaxun_updata_model.text:
        #     raise ValueError(
        #         "调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((chaxun_updata_model.status_code), chaxun_updata_model.json()))
        # elif "name" in chaxun.text:
        #     if not "修改之后" == chaxun_updata_model.json()["description"]:
        #         raise ValueError("修改优模型失败，错误原因为 : %s " % (chaxun_updata_model.json()))

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




    def tearDown(self) -> None:
        pass