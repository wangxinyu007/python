
"""进行获取token"""
import requests
from manage.getconfigparam import *
from frame_work import request_frame_work
def get_token():
    """获取登录的token"""
    login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
    headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
               "Content-Type": "application/x-www-form-urlencoded"}
    login_data = {"username": "scf_adm", "password": "Ut123456", "grant_type": "password", "scope": "read"}
    response = requests.post(url=login_url, headers=headers, data=login_data)
    access_token = response.json()["access_token"]
    Authorization_value = "bearer " + access_token
    headers1 = {"Content-Type": "application/json", "Authorization": Authorization_value}
    return  headers1

