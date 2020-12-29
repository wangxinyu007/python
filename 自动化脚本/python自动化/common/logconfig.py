#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/12 9:30
# @Author   : Mr.Gan
# @File     : set_log.py
# @Software : PyCharm


import logging
import os, time


# 初始化日志配置类
class SetLog(object):
    """
    SetLog类 划分了两个日志等级 'INFO'  'ERROR', 每天产生的日志
    会存放在根据时间生成的目录文件里面
    """
    def __init__(self):
        self._create_dir()

    @staticmethod
    def _get_dir_path(dirname):
        '''
        根据时间生成日志目录
        :param dirname: log目录下的 子目录名称
        :return: 拼接后的 目录路径
        '''
        dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"log", dirname)
        time_name = time.strftime("%Y_%m_%d")
        names = os.path.join(dir_path, time_name)
        return names

    def _create_dir(self):
        '''
        每天会生成新的日志目录存放日志  ERROR路径 INFO路径
        :return: None
        '''
        self.error_path = self._get_dir_path("error_log")
        if not os.path.exists(self.error_path):
            os.mkdir(self.error_path)
        self.info_path = self._get_dir_path("info_log")
        if not os.path.exists(self.info_path):
            os.mkdir(self.info_path)

    @staticmethod
    def __set_handers(loglevel, files):
        '''
        此函数设置 loggers对象 输出格式，文件句柄, 控制台句柄, 日志文件等级
        :param loglevel: 日志文件等级
        :param files: 日志文件路径名称
        :return: loggers对象
        '''
        loggers = logging.getLogger()
        loggers.setLevel(loglevel)
        open_file = logging.FileHandler(files, mode="a", encoding="utf8")
        format_mes = logging.Formatter("%(levelname)s %(filename)s %(asctime)s %(lineno)s %(message)s")
        cmd_f = logging.StreamHandler()
        cmd_f.setFormatter(format_mes)
        open_file.setFormatter(format_mes)
        # 判断loggers对象的 handlers属性是否为空, 为空则添加句柄
        if loggers.__dict__["handlers"] is []:
            loggers.addHandler(open_file)
            loggers.addHandler(cmd_f)
        # 不为空，则初始化为空列表, 再添加句柄
        else:
            loggers.__dict__["handlers"] = []
            loggers.addHandler(open_file)
            loggers.addHandler(cmd_f)
        return loggers

    def error(self, message):
        '''
        重写 logging类的error方法 调用此函数 会记录一条error日志
        :param message: 日志内容
        :return: None
        '''
        error_file_path = os.path.join(self.error_path, "error.txt")
        logs = self.__set_handers("ERROR", error_file_path)
        logs.error(message)

    def info(self, message):
        '''
        重写 logging类的info放法 调用此函数 会记录一条info日志
        :param message: 日志内容
        :return: None
        '''
        info_file_path = os.path.join(self.info_path, "info.txt")
        logs = self.__set_handers("INFO", info_file_path)
        logs.info(message)


if __name__ == '__main__':
    a = SetLog()
    a.info("你好")
    a.error("在基建")
