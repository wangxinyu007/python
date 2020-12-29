# import requests
# # def request(url1,headers1, param1, typed="get"):
# #     if typed == "get":
# #         response1 = requests.get(url=url1,headers=headers1, params=param1)
# #         if "utMsg" in response1.json():
# #             return response1.text
# #         else:
# #             raise ValueError("状态码错误 value=【{}】".format(response1.status_code))
# #
# #     elif typed == "post":
# #         response1= requests.post(url=url1,headers=headers1, json=param1)
# #         if response1.status_code == 200:
# #             return response1.text
# #         raise ValueError("状态码错误 value=【{}】".format(response1.status_code))
#
# url = "https://oauthuat.utcook.com/uaa/oauth/login"
# headers={"Authorization":"Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0","Content-Type":"application/x-www-form-urlencoded"}
# data = {
#     "username":"scf_dev",
#     "password":"Ut123456",
#     "grant_type":"password",
#     "scope":"read"
# }
# response11 = requests.post(url=url, headers=headers,data=data)
# # print(response.text)
# access_token=response11.json()["access_token"]
# # print(access_token)
# # a=response.json()
# # print(a.keys())
#
# #
# url2="https://mobileuat.utcook.com/utmodel/modelAdmin/createProfile"
# data2={
#   "category": "ut-service",
#   "identifier":"32j9h",
#   "name":"3oj1jh",
#   "description": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
#   "modelSource": "unilink"
# }
# Authorization_value="bearer " + access_token
# headers1={
#     "Content-Type":"text","Authorization":Authorization_value
# }
# # # print(Authorization_value)
# # response1=requests.post(url=url2,headers=headers1,json=data2)
# # print(response1.text)
#
# #
# url1="https://mobileuat.utcook.com/utmodel/modelAdmin/findProfile"
# param1={"category":"ut-service","identifier":"3188221"}
# # response1= requests.get(url=url1, headers=headers1,params=param1)
# # # print(response1.text)
# # # print(response1.status_code)
# # # # print(header1)
# # # # utMsg=response1.json()["utMsg"]
# # if "utMsg" in response1.json():
# #     print("优模型不存在，进行新建优模型")
# #     create= request(url1, headers1, param1)
# #
# # else:
# #     print("优模型存在，进行删除优模型")
#
#
# #
# def request(url1,headers1, param1, typed="get"):
#     if typed == "get":
#         response1 = requests.get(url=url1,headers=headers1, params=param1)
#         if response.status_code == 200:
#             print("成功创建优模型 优模型id为 【{}】".format(response.text))
#             return response.text
#         else:
#             print("不可以新建优模型：原因为 【{}】".format(response.json()["utMsg"]))
#             return response.json()["utMsg"]
#     elif typed == "post":
#         response1= requests.post(url=url1,headers=headers1, json=param1)
#         if "utMsg" not in response1.json():
#             return response1.text
#         raise ValueError("不可以新建优模型：原因为 value=【{}】".format(response1.json()["utMsg"]))
#
#
# def request1(url1,headers1, param1, typed="get"):
#     if typed == "get":
#         response = requests.get(url=url1,headers=headers1, params=param1)
#         if response.status_code == 200:
#             print("成功创建优模型 优模型id为 【{}】".format(response.text))
#             return response.text
#         else:
#             print("不可以新建优模型：原因为 【{}】".format(response.json()["utMsg"]))
#             return response.json()["utMsg"]
#     elif typed == "post":
#         response= requests.post(url=url1,headers=headers1, json=param1)
#         if response.status_code == 200:
#             print("成功创建优模型 优模型id为 【{}】".format(response.text))
#             print(response.status_code)
#             return response.text
#
#         else:
#             # print("调用接口失败的原因为 【{}】".format(response.json()["utMsg"]))
#             print(response.status_code)
#             return response.text
# # a=request1(url1, headers1,param1)
# # print(a)
#
#
# # c=request1(url2,headers1,data2,typed="post")
#
# # delete_url="https://mobileuat.utcook.com/utmodel/modelAdmin/delete"
# # delete_param={"category": "ut-device","identifier": "311"}
# # delete=request1(delete_url, headers1, delete_param,typed="post")
#
#
#
# delete_Property_url =  "https://mobileuat.utcook.com/utmodel/modelServiceDeveloper/create"
# data333={
#   "property": {
#     "accessMode": "r",
#     "dataType": {
#       "specs": {
#       	"min": -214648,
# 		"max": 2147483647,
# 		"step": 2
#       },
#       "type": "int"
#     },
#     "description": "ipsum occa",
#     "identifier": "22",
#     "name": "修改之后"
#   }
# }
# # Delete_Property = request1(delete_Property_url,headers1, data333,typed="post")
# # print(Delete_Property)
#
#
#
#
# import json
# create_Service_data = {"id": "5e9cff592709ae0001fe8ff9",
#   "event": {
#     "description": "aute ut id",
#     "identifier": "ss",
#     "type": "warning",
#     "name": "72",
#     "topic": "dolore"
#   }
# }
# a1=json.dumps(create_Service_data)
# print(a1)
#
#
# a2=json.loads(a1)
# print(a2)
#
# # a13=json.loads(create_Service_data)
# # print(a13)



a=[5,3,2,1,4]
b=[7,8]
c=[]
for i in a:
    a=list[lambda i:i**2]
    print(a)

print(c)
b.sort()
print(b)

