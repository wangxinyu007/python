# sum=0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i !=k ) and (j!=k) and (i !=j):
#                 print(i,j,k)
#                 sum+=1
# print(sum)
#

# i = int(input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print((i-arr[idx])*rat[idx])
#         i=arr[idx]
# print(r)
#
# i = ['a', 'b']
# l = [1, 2]
# print(dict(zip(i,l)))
# print(type())

#
# for i in range(1,10000):
#     a=i+100
#     b=i+268
#     for j in range(1,10000):
#         if (j*j==a) :
#             for k  in  range(1,10000):
#                 if (k*k==b) :
#                     print(i)
#

a="eyJ1c2VyX25hbWUiOiI0Mjk3MDE5NTY4ODEzMjM2NTQ1Iiwic2NvcGUiOlsicmVhZCJdLCJhdGkiOiJjY2I0YTQ3Ni0wOTRkLTQ5YWYtYjcyNS1lNjE5ODFiNzM1OTQiLCJleHAiOjE2MDIwNTU0NDYsImFjY291bnRTeXN0ZW1LZXkiOiJkZWZhdCIsImF1dGhvcml0aWVzIjpbInBsYXRmb3JtX2FwcF9hZGRBcHAiLCJwbGF0Zm9ybV9hY2NvdW50X2dldEFsbFVzZXJuYW1lQnlBdXRob3JpdHkiLCJwbGF0Zm9ybV9hcHBfYmluZEF1dGhHcm91cDJNZW51IiwicGxhdGZvcm1fYXBwX2RlbGV0ZU1lbnUiLCJwbGF0Zm9ybV9hcHBfcGFnZUFsbEF1dGhvcml0aWVzIiwicGxhdGZvcm1fYWNjb3VudF9wYWdlQWNjb3VudFN5c3RlbVVzZXJzIiwicGxhdGZvcm1fdXNlciIsInBsYXRmb3JtX2FwcF9jaGlsZEFjY291bnRNYW5hZ2VtZW50IiwicGxhdGZvcm1fYXBwX2NyZWF0ZUNoaWxkQWNjb3VudCIsInBsYXRmb3JtX2FwcF9tYW5hZ2VtZW50IiwicGxhdGZvcm1fYWNjb3VudF9jcmVhdGVBY2NvdW50U3lzdGVtIiwicGxhdGZvcm1fYXBwX2NoaWxkVXNlcnMiLCJhbmFseXNpc3Rvb2xfdXBkYXRlQW5hbHlzaXMiLCJkZXZlbG9wZXJfZmxvd19mbG93X2RldiIsImFuYWx5c2lzdG9vbF9hZG1pbnJvbGUiLCJmaWVsZG1vZGVsdG9vbF91cGRhdGVGaWVsZERhdGFUYWJsZSIsImRldmVsb3Blcl9hY2NvdW50X3N5c3RlbV9saXN0IiwiYW5hbHlzaXN0b29sX2NyZWF0ZUZpZWxkIiwiY2xvdWRleGVjdXRlX3Jldm9rZV9zZXJ2aWNlIiwicGxhdGZvcm1fYXBwX2JpbmRBdXRoMlVzZXIiLCJwbGF0Zm9ybV9hZG1pbiIsInBsYXRmb3JtX2FwcF9nZXRNZW51IiwicGxhdGZvcm1fYXBwIiwiYW5hbHlzaXN0b29sX2NyZWF0ZUFuYWx5c2lzIiwiZGV2ZWxvcGVyX2FwcGxpY2F0aW9uX3VzZXIiLCJwbGF0Zm9ybV9tZW51IiwicGxhdGZvcm1fYXBwX2dldEFwcCIsInBsYXRmb3JtX2FwcF9iaW5kQXV0aEdyb3VwMlVzZXIiLCJwbGF0Zm9ybV9hcHBfZW1wb3dlck1hbmFnZW1lbnQiLCJhbmFseXNpc3Rvb2xfdXBkYXRlRmllbGQiLCJwbGF0Zm9ybV9hcHBfdXBkYXRlQXBwIiwicGxhdGZvcm1fYXBwX2FsbEF1dGhvcml0eUdyb3VwcyIsImZpZWxkbW9kZWx0b29sX2NyZWF0ZUZpZWxkR2xvc3NhcnkiLCJwbGF0Zm9ybV9hcHBfYmluZEF1dGgyTWVudSIsInBsYXRmb3JtX2FwcF9kZWxldGVBdXRob3JpdHlHcm91cCIsInBsYXRmb3JtX2FwcF9hdXRob3JpdHlNYW5hZ2VtZW50IiwicGxhdGZvcm1fYXBwX3VuQmluZEF1dGgyQXV0aEdyb3VwIiwicGxhdGZvcm1fYWNjb3VudF91cGRhdGVBY2NvdW50U3lzdGVtU3RhdHVzIiwicGxhdGZvcm1fYXBwX2FkZEF1dGhvcml0eSIsInBsYXRmb3JtX2FwcF91cGRhdGVBdXRob3JpdHlHcm91cCIsInBsYXRmb3JtX2RldmVsb3BlciIsInBsYXRmb3JtX2FjY291bnRfY3JlYXRVc2VyVW5kZXJBY2NvdW50IiwicGxhdGZvcm1fbWFuYWdlbWVudCIsInBsYXRmb3JtX3BhZ2VQbGF0Zm9ybUFwcHMiLCJmaWVsZG1vZGVsdG9vbF91cGRhdGVGaWVsZEdsb3NzYXJ5IiwicGxhdGZvcm1fYXBwX2FkZEF1dGhvcml0eUdyb3VwIiwiY2xvdWRleGVjdXRlX3B1Ymxpc2hfc2VydmljZSIsInBsYXRmb3JtX2FwcF9hbGxBcHBzIiwiZGV2ZWxvcGVyX2Zsb3dfZGVwYXJ0bWVudF9kZXYiLCJwbGF0Zm9ybV9hcHBfZGVsZXRlQXV0aG9yaXR5IiwicGxhdGZvcm1fYWNjb3VudF91cGRhdGVVc2VyU3RhdHVzIiwiZGV2ZWxvcGVyX3VzZXIiLCJwbGF0Zm9ybV9hcHBfYWRkTWVudSIsInBsYXRmb3JtX2FjY291bnRfcXVlcnlVc2VyQnlBdXRoR3JvdXAiLCJwbGF0Zm9ybV9hcHBfbWVudU1hbmFnZW1lbnQiLCJmaWVsZG1vZGVsdG9vbF9kZWxldGVGaWVsZERhdGFUYWJsZSIsImZpZWxkbW9kZWx0b29sX2RlbGV0ZUZpZWxkRnVuY3Rpb24iLCJhbmFseXNpc3Rvb2xfZGVsZXRlRmllbGQiLCJmaWVsZG1vZGVsdG9vbF9hZG1pbmZpZSIsInBsYXRmb3JtX2FwcF9hbGxBdXRob3JpdGllcyIsImRldmVsb3Blcl9teUFwcGxpY2F0aW9uX3VzZXIiLCJwbGF0Zm9ybV9hY2NvdW50X3BhZ2VBY2NvdW50U3lzdGVtcyIsImZpZWxkbW9kZWx0b29sX2FkbWluZnVuIiwicGxhdGZvcm1fdXNlcl9iYXRjaFJlZ2lzdGVyIiwicGxhdGZvcm1fYXBwX2FsbE1lbnVzIiwicGxhdGZvcm1fcmVzZXRQd2QiLCJmaWVsZG1vZGVsdG9vbF9kZWxldGVGaWVsZEdsb3NzYXJ5IiwiZmllbGRtb2RlbHRvb2xfY3JlYXRlRmllbGREYXRhVGFibGUiLCJmaWVsZG1vZGVsdG9vbF91cGRhdGVGaWVsZEZ1bmN0aW9uIiwicGxhdGZvcm1fYXBwX2JpbmRBdXRoMkF1dGhHcm91cCIsInBsYXRmb3JtX2FwcF9hcHBMaXN0IiwicGxhdGZvcm1fYWNjb3VudF91cGRhdGVBY2NvdW50U3lzdGVtIiwicGxhdGZvcm1fYXV0aG9yaXR5R3JvdXAiLCJwbGF0Zm9ybV9saXN0UGxhdGZvcm1BcHBzIiwiZGV2ZWxvcGVyX2Zsb3dfZGV2IiwicGxhdGZvcm1fYXBwX3VwZGF0ZUF1dGhvcml0eSIsInBsYXRmb3JtX2FwcF91bkJpbmRBdXRoMk1lbnUiLCJwbGF0Zm9ybV9hcHBfYXV0aG9yaXR5R3JvdXBNYW5hZ2VtZW50IiwiYW5hbHlzaXN0b29sX2RlbGV0ZUFuYWx5c2lzIiwiY2xvdWRleGVjdXRlX3B1Ymxpc2hfbWFuYWdlciIsInBsYXRmb3JtX2FwcF9jaGFuZ2VBcHBTdGF0dXMiLCJwbGF0Zm9ybV9hcHBfdW5CaW5kQXV0aEdyb3VwMk1lbnUiLCJwbGF0Zm9ybV9hcHBfdXBkYXRlTWVudSIsImZpZWxkbW9kZWx0b29sX2NyZWF0ZUZpZWxkRnVuY3Rpb24iLCJhbmFseXNpc3Rvb2xfYWRtaW4iLCJwbGF0Zm9ybV9hY2NvdW50X2dldEFsbFVzZXJuYW1lQnlBdXRob3JpdHlHcm91cCIsInBsYXRmb3JtX2F1dGhvcml0eSJdLCJqdGkiOiJmZTgxYjA2Mi0wODEwLTQ3ZjItYWQyYi03MzQxMjI5YzA2ZWIiLCJjbGllbnRfaWQiOiJzc28tZ2F0ZXdheSIsInVzZXJuYW1lIjoiYXBwcm92YWxfdWF0X2RldiJ9"