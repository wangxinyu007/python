# import os
# import xlrd
#
#
# class ReadExcel:
#     @staticmethod
#     def _check_param(filename, sheet_index):
#         if os.path.isfile(filename):
#             excel=xlrd.open_workbook(filename)
#             if sheet_index <= len(excel.sheet_names())-1:
#                 excel_sheet=excel.sheet_by_index(sheet_index)
#                 return excel_sheet
#             raise  IndexError("Index error %s" % sheet_index)
#         raise ValueError("NO such file %s" % filename)
#
#
#     def read_sheet(self,filename,sheet_index):
#         execl_sheet=self._check_param(filename, sheet_index)
#         rows=execl_sheet.nrows
#         title=execl_sheet.row_values(0)
#         api_data_list=[]
#         for index in range(1,rows):
#             api_data_list.append(dict(zip(title,execl_sheet.row_values(index))))
#         return api_data_list
#
#
# if __name__ == '__main__':
#     print(ReadExcel().read_sheet(r"C:\Users\26224\Desktop\个人\wxyyy\day\test.xls",0))

'''
Author: xiaomin
Date: 2020-12-16 15:44:03
'''
import os
import sys
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import xlrd
import time
from common.logconfig import *


def read_xlrd(excel_file):
    '''读取excel所有数据'''
    try:
        data=xlrd.open_workbook(excel_file)
        # table=data.sheet_by_index(0)
        sheets=data.sheet_names()
        #获取所有的下标
        datafile=[]
        now=int(round(time.time() * 1000))
        for sheet in sheets:
            table=data.sheet_by_name(sheet)
            #计算每个表 有多少行
            for rowNum in range(table.nrows):
                #去掉表头,替换时间戳标志
                if rowNum>0:
                    rowdata=table.row_values(rowNum)
                    #将<time_stamp> 换成时间戳。数据随机 不重复
                    rowData=[str(i).replace('<time_stamp>',str(now)) for i in rowdata]
                    datafile.append(rowData)
    except Exception as e:
        # MyLog.error('\033[31m {} \033[0m'.format(e))
        SetLog.error('\033[31m {} \033[0m'.format(e))
        raise

    return datafile

class InitData():
    '''初始化excel数据'''
    def __init__(self,datafile,case_no):
        #case_no用例编号索引
        self.datafile=datafile
        self.case_id=[]
        self.case_module=[]
        self.case_name=[]
        self.username=[]
        self.password=[]
        self.method=[]
        self.url_path=[]
        self.api_type=[]
        self.headers=[]
        self.request_body=[]
        self.status_code=[]
        self.resp_expect=[]
        self.resp_current=[]
        self.case_no=case_no

    def get_data(self):
        self.case_id=self.datafile[self.case_no][0]
        self.case_module=self.datafile[self.case_no][1]
        self.case_name=self.datafile[self.case_no][2]
        self.username=self.datafile[self.case_no][3]
        self.password=self.datafile[self.case_no][4]
        self.method=self.datafile[self.case_no][5]
        self.url_path=self.datafile[self.case_no][6]
        self.api_type=self.datafile[self.case_no][7]
        self.headers=self.datafile[self.case_no][8]
        self.request_body=self.datafile[self.case_no][9]
        self.status_code=self.datafile[self.case_no][10]
        self.resp_expect=self.datafile[self.case_no][11]
        self.resp_current=self.datafile[self.case_no][12]




if __name__=="__main__":
    excel_file=r"C:\Users\26224\Desktop\个人\wxyyy\day\test.xls"
    testcase=read_xlrd(excel_file)
    print(testcase)
    # a=InitData(excel_file,0)
    # a.get_data()
    # print(a.case_id)
    # print(a.case_name)
    # eval(a.headers)
    # print(a.headers)