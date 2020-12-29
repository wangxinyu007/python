#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/12 9:27
# @Author   : Mr.Gan
# @File     : read_conf.py
# @Software : PyCharm


import configparser
import os


# 获取配置文件路径
conf_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "manage", "api_test.ini")

# 读取配置文件
conf = configparser.ConfigParser()
conf.read(conf_path, encoding="utf8")

pop3 = conf.get("POP3", "pop3")

my_qq = conf.get("MY_QQ", "my_qq")
qq_01 = conf.get("TO_QQ", "qq_01")

jh_url = conf.get("JH_URL", "jh_url")

tile = conf.get("TITLE", "title")

tests_user = conf.get("TESTS_USER", "tests_user")
tests_dir = conf.get("TESTS_DIR", "tests_dir")
tests_file = conf.get("TESTS_FILE", "tests_file")

getmodel_param=conf.get("CHAXUN_PARAM","getmodel_param")
create_param=conf.get("CREATE_PARAM","create_param")
create_Property_data=conf.get("CREATE_PROPERTY_DATA","create_Property_data")
create_Service_data=conf.get("CREATE_SERVICE_DATA","create_Service_data")
create_Event_data=conf.get("CREATE_EVENT_DATA","create_Event_data")
updata_param=conf.get("UPDATA_PARAM","updata_param")
updata_Property_data=conf.get("UPDATA_PROPERTY_DATA","updata_Property_data")
updata_Service_data=conf.get("UPDATA_SERVICE_DATA","updata_Service_data")
updata_Event_data=conf.get("UPDATA_EVENT_DATA","updata_Event_data")
login_data=conf.get("LOGIN_DATA","login_data")

getModel_url=conf.get("GRTMODEL_URL", "getModel_url")