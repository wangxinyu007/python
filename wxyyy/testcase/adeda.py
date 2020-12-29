import requests
login_url = "https://oauthuat.utcook.com/uaa/oauth/login"
headers = {"Authorization": "Basic c3NvLWdhdGV3YXk6c3NvLWdhdGV3YXktc2VjcmV0",
           "Content-Type": "application/x-www-form-urlencoded"}
login_data = {"username": "developer_app_admin", "password": "Ut123456", "grant_type": "password", "scope": "read"}
response = requests.post(url=login_url, headers=headers, data=login_data)
access_token = response.json()["access_token"]
Authorization_value = "bearer " + access_token
global headers1
headers1 = {"Content-Type": "application/json", "Authorization": Authorization_value}

Accountget_url = "https://mobileuat.utcook.com/settle/settlementAccount/get"
Accountget_data = {"appId":"app_abcd123"}
response_Accountget = requests.get(url=Accountget_url, headers=headers1, params=Accountget_data)
print(response_Accountget.text)