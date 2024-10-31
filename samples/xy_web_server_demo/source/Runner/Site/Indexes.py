# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Index"
"""
  * @File    :   Index.py
  * @Time    :   2024/10/30 10:59:50
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""
from tornado.web import RequestHandler

# from xy_request_handler_web.Web import Web


class Index(RequestHandler):
    # class Index(Web):

    def get(self):
        self.write("xy_web_server_demo Hello World !!!")
