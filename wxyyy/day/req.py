import requests

from frame_work import request_frame_work
class SendRequest:
    def send_request(self,dist):
        tesecase_name=dist.get("用例标题")
        typed=dist.get("相关需求")
        url=(dist.get("url"))
        header=eval(dist.get("前置条件"))
        api_data=eval(dist.get("步骤"))
        if typed == "get":
            response = request_frame_work.request1(url, header, api_data).text
        else:
            response = request_frame_work.request1(url, header, api_data, typed="post").text

        return response,tesecase_name