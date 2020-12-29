# !/usr/bin/env python
# -*- coning: utf-8 -*-
# @Time     : 2019/10/23 14:26
# @Author   : Mr.Gan
# Software  : PyCharm
import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from HTMLTestRunner import HTMLTestRunner
import unittest
import time,os

from common import reportconfig


if __name__ == '__main__':
    reportconfig.SetReport()
    # test_dir = 'C:\\Users\\26224\\Desktop\\个人\\api_test_0820\\testcase'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='ye*.py')
    #
    # now = time.strftime('%Y-%m-%d %H_%M_%S')
    # # 定义报告存放路径
    # filename = 'C:\\Users\\26224\\Desktop\\个人\\api_test_0820\\Report\\report' + now + 'result.html'
    # fp = open(filename, 'wb')
    # # 定义测试报告
    # runner = HTMLTestRunner(stream=fp, title='dev_api测试报告', description='用例执行情况:')
    # runner.run(discover,rerun=0, save_last_run=False)
    # fp.close()