# import xlwt;
# import xlrd;
# # import xlutils;
#
#
# # init xls file
# # styleBlueBkg= xlwt.easyxf('pattern: pattern solid, fore_colour sky_blue;');
# # styleBold   = xlwt.easyxf('font: bold on');
#
# wb = xlwt.Workbook()
# ws = wb.add_sheet("zx.xls")
# ws.write(0, 0, "Header")
# ws.write(0, 1, "CatalogNumber")
# ws.write(0, 2, "PartNumber")
# wb.save("zx.xls")
#
# from xlutils.copy import copy;
# import xlwt
# f = xlwt.Workbook() #创建百工作簿度
# sheet1 = f.add_sheet(u'zzx.sheet1',cell_overwrite_ok=True) #创建sheet
# # list=[1,2,3,4,5]
# # j = 0
# # for i in list:
# #     sheet1.write(j,0,i) #循环写入 竖着版写
# #     j =j+1
# # f.save('text11.xls')#保存文件权
#
# for i in range(1,10):
#
#
#     sheet1.write(i, 9, 1)  # 循环写入 竖着版写
# f.save('text11.xls')#保存文件权
import json


import requests
url="https://oauthuat2.utcook.com/uaa/authentication/form"
headers={"Content-Type":"application/x-www-form-urlencoded","Authorization":"Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0"}
data={"mobile":"18925208684","password":"Ut123456"}
print(data)
print(type(data))
json_param= json.dumps(data)
print(json_param)
response=requests.post(url=url,headers=headers,data=data)
print(response.content.decode('utf-8'))