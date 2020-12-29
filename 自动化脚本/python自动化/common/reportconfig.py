#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/12 11:36
# @Author   : Mr.Gan
# @File     : set_report.py
# @Software : PyCharm


import unittest
import HTMLTestRunner
import time
import os
import smtplib

from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart

from common import logconfig
from manage.getconfigparam import *

logs = logconfig.SetLog()


class SetReport(object):
    """
    此类封装了3个功能, _get_suite 获取测试套件, _set_report 生成测试报告
    _send_email方法 发送报告附件,  _send_email为入口
    """

    def __init__(self):
        self._create_dir()
        self._set_report()
        # self._send_email()

    @staticmethod
    def _get_dir_path():
        '''
        根据时间生成日志目录
        :param dirname: log目录下的 子目录名称
        :return: 拼接后的 目录路径
        '''
        dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"report")
        time_name = time.strftime("%Y_%m_%d")
        names = os.path.join(dir_path, time_name)
        return names

    def _create_dir(self):
        '''
        :return: None
        '''
        self.report_path = self._get_dir_path()
        if not os.path.exists(self.report_path):
            os.mkdir(self.report_path)

    def _get_suite(self):
        '''
        获取测试用例集合，添加到测试套件
        :return: 测试套件对象
        '''
        suite = unittest.TestSuite()
        tests = unittest.defaultTestLoader.discover(
            start_dir=tests_dir,
            pattern=tests_file
        )
        for test in tests:
            # for i in test:
                suite.addTests(test)
        return suite

    def _set_report(self):
        '''
        配置测试报告参数, 以时间来命名， 生成 html格式的测试报告
        :return: None
        '''
        self.times = time.strftime("%H_%M_%S") + "_report.html"
        self.html_path = os.path.join(self.report_path, self.times)
        with open(self.html_path, "wb") as f:
            h = HTMLTestRunner.HTMLTestRunner(
                f,
                title=tile,
                description=tests_user
            )
            h.run(self._get_suite())

    def _send_email(self):
        '''
        测试报告生成后，把测试报告以附件的方式 发送QQ邮件,
        :return: None
        '''
        try:
            self._set_report()
            msg = MIMEMultipart()
            msg['From'] = formataddr(["大佬", my_qq])
            msg['To'] = formataddr(["小弟", qq_01])
            msg['Subject'] = "自动化邮件"
            msg.attach(MIMEText('今日份的测试报告,请签收', 'html', 'utf-8'))
            with open(self.html_path, 'rb') as f:
                mime = MIMEBase('image', 'html', filename=self.times)
                mime.add_header('Content-Disposition', 'attachment', filename=self.times)
                mime.add_header('Content-ID', '<0>')
                mime.add_header('X-Attachment-Id', '0')
                mime.set_payload(f.read())
                encoders.encode_base64(mime)
                msg.attach(mime)
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)
            server.login(my_qq, pop3)
            server.sendmail(my_qq, [qq_01], msg.as_string())
            server.quit()
            logs.info("邮件发送成功, 发件人{}, 接收人{}".format(my_qq, qq_01))
        except Exception as e:
            logs.error(e)
            exit(-1)


if __name__ == '__main__':
    SetReport()
