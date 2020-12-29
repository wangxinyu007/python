
from ddt import data, ddt, unpack, file_data
import unittest
import os
import xlrd
from day import sss
from day import req
from xlutils.copy import copy

d=sss.ReadExcel().read_sheet(r"C:\Users\26224\Desktop\个人\wxyyy\day\用户中心-用例.xlsx",0)

rb= xlrd.open_workbook(r"C:\Users\26224\Desktop\个人\wxyyy\day\用户中心-用例.xlsx")
wb = copy(rb)
ws = wb.get_sheet(0)
global n
n = []
@ddt
class A(unittest.TestCase):

    def setUp(self) -> None:
        self.a=req.SendRequest()

    @data(*d)
    def test_01(self, k):
        response,testcase_name=self.a.send_request(k)
        n.append(response)


        # return response
        # self.assertEquals(response,k.get("expected_results"),msg=testcase_name)

    # @file_data(r"D:\aaa.json",  "D:aaa.xml")
    # def test_03(self, value):
    #     pass

# 定义一个类，这个类负责打开execl，读取数据，把读取完的数据 以list储存
    # 如 [{"testcase_name": 用例名称, "typed": 请求方式, "url": url, "api_data": 数据, "预期结果": 结果},
    #   {"testcase_name": 用例名称, "typed": 请求方式, "url": url, "api_data": 数据, "预期结果": 结果},
        #{"testcase_name": 用例名称, "typed": 请求方式, "url": url, "api_data": 数据, "预期结果": 结果},
    # ] 把这个数据 return

# 定义一个类，这个类负责 发送请求，返回 response



# 用例类，使用 ddt来完成数据驱动测试，对比预期结果与返回的response，


    def tearDown(self) -> None:

        # for i in range(1, 10):
        #     ws.write(i, 16, globals()["a"])  # 循环写入 竖着版写
        # wb.save('text11.xls')  # 保存文件权
        pass

    @classmethod
    def tearDownClass(cls):
        m=1
        for i in n:
            ws.write(m, 20, i)  # 循环写入 竖着版写
            m+=1

        if os.path.exists(r"C:\Users\26224\Desktop\wxyyy\day\text11.xls"):
            os.remove(r"C:\Users\26224\Desktop\wxyyy\day\text11.xls")
        else:
            wb.save('text11.xls')  # 保存文件权


if __name__ == '__main__':
    unittest.main()