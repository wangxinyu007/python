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


class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        global description
        description = "更改之前"
        global updata_description
        updata_description="更改之后"

        """获取登录的token"""
        login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
        headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
                   "Content-Type": "application/x-www-form-urlencoded"}
        login_data = {"username": "scf_adm", "password": "Ut123456", "grant_type": "password", "scope": "read"}
        response = requests.post(url=login_url, headers=headers, data=login_data)
        access_token = response.json()["access_token"]
        Authorization_value = "bearer " + access_token
        global headers1
        headers1 = {"Content-Type": "application/json", "Authorization": Authorization_value}
        print(headers1)

    def test_01(self):
        """进行查询优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "112"}
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getModelProfileByKeyUsingGET_param)

        """进行判断，如果没有报错信息。说明优模型存在，进行删除优模型，
                     如果有报错信息，说明没有优模型存在，进行创建优模型"""
        if "utMsg" not in getModelProfileByKeyUsingGET.json():
            deleteModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/delete"
            deleteModelProfileByKeyUsingPOST_param = {"category": "ut-device", "identifier": "112"}
            deleteModelProfileByKeyUsingPOST = request_frame_work.request1(deleteModelProfileByKeyUsingPOST_url, headers1, deleteModelProfileByKeyUsingPOST_param,typed="post")
            # self.assertEqual(200, deleteModelProfileByKeyUsingPOST.status_code, "调用  删除优模型  接口失败。状态码错误")
            """这里进行判断， 删除成功的话返回为空。如果出现报错信息，说明接口调用错误"""
            if "utMsg"  in deleteModelProfileByKeyUsingPOST.text:
                raise ValueError("调用   删除优模型接口  失败,状态码为: %s ,返回信息为：%s" % ((deleteModelProfileByKeyUsingPOST.status_code), deleteModelProfileByKeyUsingPOST.json()))
            else:
                """进行创建优模型"""
                createModelProfileUsingPOST_url = jh_url + "/modelAdmin/createProfile"
                createModelProfileUsingPOST_param = {"category": "ut-device", "identifier": "112", "name": "更改之前","description": description, "modelSource": "unilink"}
                createModelProfileUsingPOST = request_frame_work.request1(createModelProfileUsingPOST_url, headers1,createModelProfileUsingPOST_param,typed="post")
                self.assertEqual(200, createModelProfileUsingPOST.status_code, "调用  进行创建优模型  接口失败。状态码错误")
        else:
            """进行创建优模型"""
            createModelProfileUsingPOST_url=jh_url +"/modelAdmin/createProfile"
            createModelProfileUsingPOST_param={"category": "ut-device","identifier":"112","name":"更改之前","description": description}
            createModelProfileUsingPOST=request_frame_work.request1(createModelProfileUsingPOST_url, headers1, createModelProfileUsingPOST_param,typed="post")
            self.assertEqual(200, createModelProfileUsingPOST.status_code, "调用  进行创建优模型  接口失败。状态码错误")

        """新建属性"""
        createThingPropertyUsingPOST_url=jh_url +"/modelPropertyAdmin/create"
        createThingPropertyUsingPOST_param={"modelId": createModelProfileUsingPOST.text,"identifier": "shuxing", "name": "属性更改之前", "accessMode": "rw", "dataType": {"specs": {"0": "11", "1": "1"}, "type": "bool"}, "description": description}
        createThingPropertyUsingPOST= request_frame_work.request1(createThingPropertyUsingPOST_url, headers1, createThingPropertyUsingPOST_param, typed="post")
        if "utMsg"  in createThingPropertyUsingPOST.text:
            raise ValueError("调用  新建属性  接口失败,状态码为: %s ,返回信息为：%s" % ((createThingPropertyUsingPOST.status_code), createThingPropertyUsingPOST.json()))
        else:
            pass
        """修改属性"""
        updateThingPropertyUsingPOST_url = jh_url + "/modelPropertyAdmin/update"
        updateThingPropertyUsingPOST_data={"id": createThingPropertyUsingPOST.text,"property": {"accessMode": "r", "dataType": {"specs": {"min": -214648, "max": 2147483647, "step": 2}, "type": "int"}, "description": updata_description, "identifier": "updata_Property_data", "name": "修改属性之后"}}
        updateThingPropertyUsingPOST = request_frame_work.request1(updateThingPropertyUsingPOST_url, headers1,updateThingPropertyUsingPOST_data,typed="post")
        if "utMsg"  in updateThingPropertyUsingPOST.text:
            raise ValueError("调用  修改属性  接口失败,状态码为: %s ,返回信息为：%s" % ((updateThingPropertyUsingPOST.status_code), updateThingPropertyUsingPOST.json()))
        else:
            pass
        """查询属性"""
        findThingPropertyUsingGET_url=jh_url+ "/modelPropertyAdmin/find"
        findThingPropertyUsingGET_data={"id": createThingPropertyUsingPOST.text}
        findThingPropertyUsingGET= request_frame_work.request1(findThingPropertyUsingGET_url, headers1, findThingPropertyUsingGET_data)
        # self.assertEqual(200, findThingPropertyUsingGET.status_code, "调用  查询属性  接口失败。状态码错误")
        if "utMsg"  in findThingPropertyUsingGET.text:
            raise ValueError("调用  修改属性  接口失败,状态码为: %s ,返回信息为：%s" % ((findThingPropertyUsingGET.status_code), findThingPropertyUsingGET.json()))
        else:
            if  "更改之后" != findThingPropertyUsingGET.json()["description"]:
                # raise ValueError("修改属性失败,未修改成功，错误原因为 : %s " % (findThingPropertyUsingGET.json()))
                raise ValueError("修改属性失败,未修改成功，状态码为: %s ,返回信息为：%s" % ((findThingPropertyUsingGET.status_code), findThingPropertyUsingGET.json()))
        """删除属性"""
        deleteThingPropertyUsingPOST_url=jh_url+ "/modelPropertyAdmin/delete"
        deleteThingPropertyUsingPOST_data = createThingPropertyUsingPOST.text
        deleteThingPropertyUsingPOST = requests.post(url=deleteThingPropertyUsingPOST_url, headers=headers1, data=deleteThingPropertyUsingPOST_data)
        # self.assertEqual(200, deleteThingPropertyUsingPOST.status_code, "调用  删除属性  接口失败。状态码错误")
        if "utMsg" in deleteThingPropertyUsingPOST.text:
            raise ValueError("调用  删除属性  接口失败,状态码为: %s ,返回信息为：%s" % ((deleteThingPropertyUsingPOST.status_code), deleteThingPropertyUsingPOST.json()))
        else:
            pass

        """新建服务"""
        createThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/create"
        createThingServiceUsingPOST_data2={"modelId": createModelProfileUsingPOST.text,"identifier": "service", "name": "服务更改之前", "inputData": [], "outputData": [], "callType": "async", "requestMethod": "delete", "url": "exercitation Duis ex", "description": description}
        createThingServiceUsingPOST = request_frame_work.request1(createThingServiceUsingPOST_url, headers1, createThingServiceUsingPOST_data2, typed="post")
        # self.assertEqual(200, createThingServiceUsingPOST.status_code, "调用  新建服务  接口失败。状态码错误")
        if "utMsg" in createThingServiceUsingPOST.text:
            raise ValueError("调用  新建服务  接口失败,状态码为: %s ,返回信息为：%s" % ((createThingServiceUsingPOST.status_code), createThingServiceUsingPOST.json()))
        else:
            pass
        """修改服务"""
        updateThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/update"
        updateThingServiceUsingPOST_data2={"id": createThingServiceUsingPOST.text,"service": {"identifier": "service", "name": "服务更改之后", "inputData": [], "outputData": [], "callType": "async", "requestMethod": "delete", "url": "exercitation Duis ex", "description": updata_description}}
        updateThingServiceUsingPOST = request_frame_work.request1(updateThingServiceUsingPOST_url, headers1, updateThingServiceUsingPOST_data2,typed="post")
        # self.assertEqual(200, updateThingServiceUsingPOST.status_code, "调用  编辑服务  接口失败。状态码错误")
        if "utMsg" in updateThingServiceUsingPOST.text:
            raise ValueError("调用  修改服务  接口失败,状态码为: %s ,返回信息为：%s" % ((updateThingServiceUsingPOST.status_code), updateThingServiceUsingPOST.json()))
        else:
            pass
        """查询服务"""
        findThingServiceUsingGET_url = jh_url + "/modelServiceAdmin/find"
        findThingServiceUsingGET_data={"id": createThingServiceUsingPOST.text}
        findThingServiceUsingGET = request_frame_work.request1(findThingServiceUsingGET_url, headers1, findThingServiceUsingGET_data)
        # self.assertEqual(200, findThingServiceUsingGET.status_code, "调用  查询服务  接口失败。状态码错误")
        if "utMsg" in findThingServiceUsingGET.text:
            raise ValueError("调用  修改服务  接口失败,状态码为: %s ,返回信息为：%s" % ((findThingServiceUsingGET.status_code), findThingServiceUsingGET.json()))
        else:
            if  "更改之后" != findThingServiceUsingGET.json()["description"]:
                raise ValueError("修改服务失败,未修改成功，状态码为: %s ,返回信息为：%s" % ((findThingPropertyUsingGET.status_code), findThingPropertyUsingGET.json()))
            else:
                pass
        """删除服务"""
        deleteThingServiceUsingPOST_url = jh_url + "/modelServiceAdmin/delete"
        deleteThingServiceUsingPOST_data=createThingServiceUsingPOST.text
        deleteThingServiceUsingPOST = requests.post(url=deleteThingServiceUsingPOST_url, headers=headers1,data=deleteThingServiceUsingPOST_data)
        # self.assertEqual(200, deleteThingPropertyUsingPOST.status_code, "调用  删除属性  接口失败。状态码错误")
        if "utMsg" in deleteThingServiceUsingPOST.text:
            raise ValueError("调用  删除服务  接口失败,状态码为: %s ,返回信息为：%s" % ((deleteThingServiceUsingPOST.status_code), deleteThingServiceUsingPOST.json()))
        else:
            pass
        """新建事件"""
        createThingEventUsingPOST_url = jh_url + "/modelEventAdmin/create"
        createThingEventUsingPOST_data={"modelId": createModelProfileUsingPOST.text,"identifier": "device","name": "事件更改之前","type": "warning","outputData": [],"description": description,"topic": "sed aliqua"}
        createThingEventUsingPOST = request_frame_work.request1(createThingEventUsingPOST_url, headers1, createThingEventUsingPOST_data, typed="post")
        # self.assertEqual(200, createThingEventUsingPOST.status_code, "调用  新建事件  接口失败。状态码错误")
        if "utMsg" in createThingEventUsingPOST.text:
            raise ValueError("调用  新建事件  接口失败,状态码为: %s ,返回信息为：%s" % ((createThingEventUsingPOST.status_code), createThingEventUsingPOST.json()))
        else:
            pass
        """修改事件"""
        updateThingEventUsingPOST_url = jh_url + "/modelEventAdmin/update"
        updateThingEventUsingPOST_data={ "id": createThingEventUsingPOST.text,"event": {"identifier": "device","name": "修改事件之后","type": "warning","outputData": [],"description": updata_description,"topic": "sed aliqua"}}
        updateThingEventUsingPOST = request_frame_work.request1(updateThingEventUsingPOST_url, headers1, updateThingEventUsingPOST_data,typed="post")
        # self.assertEqual(200, updateThingEventUsingPOST.status_code, "调用  编辑事件  接口失败。状态码错误")
        if "utMsg" in updateThingEventUsingPOST.text:
            raise ValueError("调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((updateThingEventUsingPOST.status_code), updateThingEventUsingPOST.json()))
        else:
            pass
        """查询事件"""
        findThingEventUsingGET_url = jh_url + "/modelEventAdmin/find"
        findThingEventUsingGET_data={"id": createThingEventUsingPOST.text}
        findThingEventUsingGET = request_frame_work.request1(findThingEventUsingGET_url, headers1, findThingEventUsingGET_data)
        # self.assertEqual(200, findThingEventUsingGET.status_code, "调用  查询事件  接口失败。状态码错误")
        if "utMsg" in findThingEventUsingGET.text:
            raise ValueError("调用  修改事件  接口失败,状态码为: %s ,返回信息为：%s" % ((findThingEventUsingGET.status_code), findThingEventUsingGET.json()))
        else:
            if not "更改之后" == findThingEventUsingGET.json()["description"]:
                raise ValueError("修改事件失败,未修改成功，状态码为: %s ,返回信息为：%s" % ((findThingEventUsingGET.status_code), findThingEventUsingGET.json()))
            else:
                pass
        """删除事件"""
        deleteThingEventUsingPOST_url = jh_url + "/modelEventAdmin/delete"
        deleteThingEventUsingPOST_data=createThingEventUsingPOST.text
        deleteThingEventUsingPOST = requests.post(url=deleteThingEventUsingPOST_url, headers=headers1,data=deleteThingEventUsingPOST_data)
        # self.assertEqual(200, deleteThingEventUsingPOST.status_code, "调用  删除属性  接口失败。状态码错误")
        if "utMsg" in deleteThingEventUsingPOST.text:
            raise ValueError("调用  删除事件  接口失败,状态码为: %s ,返回信息为：%s" % ((deleteThingEventUsingPOST.status_code), deleteThingEventUsingPOST.json()))
        else:
            pass
        """修改优模型"""
        updateModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/updateProfile"
        updateModelProfileByKeyUsingPOST_param={"category": "ut-device","identifier":"112","description": updata_description}
        updateModelProfileByKeyUsingPOST = request_frame_work.request1(updateModelProfileByKeyUsingPOST_url, headers1, updateModelProfileByKeyUsingPOST_param, typed="post")
        # self.assertEqual(200, updateModelProfileByKeyUsingPOST.status_code, "调用  编辑优模型  接口失败。状态码错误")
        if "utMsg" in updateModelProfileByKeyUsingPOST.text:
            raise ValueError("调用  修改优模型  接口失败,状态码为: %s ,返回信息为：%s" % ((updateModelProfileByKeyUsingPOST.status_code), updateModelProfileByKeyUsingPOST.json()))
        else:
            pass
        """查询被修改的优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "112"}
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getModelProfileByKeyUsingGET_param)
        if "utMsg" in getModelProfileByKeyUsingGET.text:
            raise ValueError("调用  查询优模型  接口失败,状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
        else:
            if not "更改之后" == getModelProfileByKeyUsingGET.json()["description"]:
                raise ValueError("修改优模型失败，错误原因为 : %s " % (getModelProfileByKeyUsingGET.json()))
            else:
                pass
        """删除优模型"""
        deleteModelProfileByKeyUsingPOST_url = jh_url + "/modelAdmin/delete"
        deleteModelProfileByKeyUsingPOST_param={"category": "ut-device","identifier": "112"}
        deleteModelProfileByKeyUsingPOST = request_frame_work.request1(deleteModelProfileByKeyUsingPOST_url, headers1, deleteModelProfileByKeyUsingPOST_param, typed="post")
        if "utMsg" in deleteModelProfileByKeyUsingPOST.text:
            raise ValueError("调用   删除优模型接口  失败,状态码为: %s ,返回信息为：%s" % ((deleteModelProfileByKeyUsingPOST.status_code), deleteModelProfileByKeyUsingPOST.json()))
        else:
            pass
        """查询被删除优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "112"}
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getModelProfileByKeyUsingGET_param)
        # if not "无效的分类或标识符" == getModelProfileByKeyUsingGET.json()["utMsg"]:
        #     raise ValueError("调用  查询被删除的优模型  接口失败,状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
        self.assertEqual(409, getModelProfileByKeyUsingGET.status_code, "调用  查询被删除的优模型  接口失败。状态码错误")
        self.assertEqual("无效的分类或标识符",getModelProfileByKeyUsingGET.json()["utMsg"], "返回信息不匹配")

    def test_02(self):
        """进行查询优模型"""
        getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
        getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "31"}
        getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getModelProfileByKeyUsingGET_param)
        """进行判断，如果没有报错信息。说明优模型存在，可以进行导入优模型进行修改，
                     如果有报错信息，说明没有优模型存在，进行创建优模型"""
        if "utMsg" not in getModelProfileByKeyUsingGET.json():
            """这里进行两次导入优模型进行修改。 防止第一次更改的，跟原有的优模型数据一样。 第二次再次进行修改，保证导入修改优模型接口正常"""
            """第一次导入优模型进行修改"""
            importSpecificationUsingPOST_url=jh_url +"/modelAdmin/importSpecification"
            importSpecificationUsingPOST_param={"profile": {"category": "ut-device","description": description,"identifier": "112","name": description},
                                                "properties": [{"accessMode": "r", "dataType": {"specs": {"min": -214648, "max": 2147483647, "step": 2}, "type": "int"}, "description": "修改属性之后", "identifier":"updata_Property_data", "name": "修改属性之后"}],
                                                "services": [{"identifier": "service", "name": "服务更改之后", "inputData": [], "outputData": [], "callType": "async", "requestMethod": "delete", "url": "exercitation Duis ex", "description": "修改服务之后"}],
                                                "events": [{"identifier": "device","name": "修改事件之后","type": "warning","outputData": [],"description": "修改事件之后","topic": "sed aliqua"}]}
            importSpecificationUsingPOST=request_frame_work.request1(importSpecificationUsingPOST_url, headers1,importSpecificationUsingPOST_param,typed="post")
            if "utMsg" in importSpecificationUsingPOST.text:
                raise ValueError("调用  第一次导入优模型进行修改接口  失败,状态码为: %s ,返回信息为：%s" % ((importSpecificationUsingPOST.status_code), importSpecificationUsingPOST.json()))

            """第一次进行查询"""
            getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
            getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "112"}
            getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getModelProfileByKeyUsingGET_param)
            if "utMsg" in getModelProfileByKeyUsingGET.text:
                raise ValueError("调用  第一次查询优模型  接口失败,状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
            else:
                if not "更改之前" == getModelProfileByKeyUsingGET.json()["description"]:
                    raise ValueError("第一次修改优模型失败，错误原因为 失败,状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
                else:
                    pass

            """第二次通过导入优模型进行修改"""
            importSpecificationUsingPOST_url = jh_url + "/modelAdmin/importSpecification"
            importSpecificationUsingPOST_param = {
                "profile": {"category": "ut-device", "description": updata_description, "identifier": "112", "name": "更改之后"},
                "properties": [{"accessMode": "r",
                                "dataType": {"specs": {"min": -214648, "max": 2147483647, "step": 2}, "type": "int"},
                                "description": "修改属性之后", "identifier": "updata_Property_data", "name": "修改属性之后"}],
                "services": [
                    {"identifier": "service", "name": "服务更改之后", "inputData": [], "outputData": [], "callType": "async",
                     "requestMethod": "delete", "url": "exercitation Duis ex", "description": "修改服务之后"}],
                "events": [
                    {"identifier": "device", "name": "修改事件之后", "type": "warning", "outputData": [], "description": "修改事件之后",
                     "topic": "sed aliqua"}]}
            importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,importSpecificationUsingPOST_param, typed="post")
            if "utMsg" in importSpecificationUsingPOST.text:
                raise ValueError("调用  第二次导入优模型进行修改接口  失败,状态码为: %s ,返回信息为：%s" % (
                (importSpecificationUsingPOST.status_code), importSpecificationUsingPOST.json()))
            """导入优模型进行修改之后，进行查询"""
            getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
            getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "112"}
            getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getModelProfileByKeyUsingGET_param)
            if "utMsg" in getModelProfileByKeyUsingGET.text:
                raise ValueError("调用  第二次查询优模型  接口失败,状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
            else:
                if not "更改之后" == getModelProfileByKeyUsingGET.json()["description"]:
                    raise ValueError("第二次修改优模型失败，错误原因为 失败,状态码为: %s ,返回信息为：%s" % ((getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
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
            importSpecificationUsingPOST = request_frame_work.request1(importSpecificationUsingPOST_url, headers1,importSpecificationUsingPOST_param, typed="post")
            if "utMsg" in importSpecificationUsingPOST.text:
                raise ValueError("调用  导入优模型进行创建优模型  接口  失败,状态码为: %s ,返回信息为：%s" % (
                    (importSpecificationUsingPOST.status_code), importSpecificationUsingPOST.json()))
            """导入优模型进行修改之后，进行查询"""
            getModelProfileByKeyUsingGET_url = jh_url + "/modelAdmin/findProfile"
            getModelProfileByKeyUsingGET_param = {"category": "ut-device", "identifier": "112"}
            getModelProfileByKeyUsingGET = request_frame_work.request1(getModelProfileByKeyUsingGET_url, headers1,getModelProfileByKeyUsingGET_param)
            if "utMsg" in getModelProfileByKeyUsingGET.text:
                raise ValueError("调用  查询导入优模型进行创建优模型  接口失败,状态码为: %s ,返回信息为：%s" % (
                (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
            else:
                if not "更改之前" == getModelProfileByKeyUsingGET.json()["description"]:
                    raise ValueError("导入优模型进行创建优模型，错误原因为 失败,状态码为: %s ,返回信息为：%s" % (
                    (getModelProfileByKeyUsingGET.status_code), getModelProfileByKeyUsingGET.json()))
                else:
                    pass



    def tearDown(self) -> None:
        pass