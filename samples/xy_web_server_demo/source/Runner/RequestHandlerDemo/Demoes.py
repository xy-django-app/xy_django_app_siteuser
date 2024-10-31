# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Demoes"
"""
  * @File    :   Demoes.py
  * @Time    :   2024/10/30 19:48:10
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from xy_request_handler_api.Api import Api


class Demo(Api):
    def check_xsrf_cookie(self) -> None:
        return None

    def check_origin(self, _):
        return False

    def post(self):
        json_arguments = self.json_arguments
        self.success()
        self.data = {
            "resp_data_json": json_arguments,
        }
        self.xy_response()


"""
# 以下是示例代码，需要在您的应用中实现
# 用来进行测试接口请求
# Python解释器运行以下代码
import requests
post_json_data = {"test":"post json data text"}
url = "http://127.0.0.1:8400/demo"
resp = requests.post(url, json=post_json_data)
resp_json = resp.json()
{'code': 0,
 'message': '请求成功',
 'data': {'resp_data_json': {'test': 'post json data text'}}}
"""
