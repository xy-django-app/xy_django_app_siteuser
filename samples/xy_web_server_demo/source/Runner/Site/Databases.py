# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "Databases"
"""
  * @File    :   Databases.py
  * @Time    :   2024/10/30 11:13:46
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""


from tornado.web import RequestHandler

# from xy_request_handler_api.Api import Api
from Demo.models import MDemo


class Query(RequestHandler):
    # class Index(Api):

    def get(self):
        output = ""
        demos = MDemo.objects.all()
        for demo in demos:
            output += (
                f"ID: {demo.id}, Identifier: {demo.identifier}, Text: {demo.text} <br/>"
            )
        self.write(f"Query: =>  <br/> {output}")


class Add(RequestHandler):
    # class Add(Api):
    @property
    def text(self):
        text = self.get_argument("text", default="")
        return text

    def get(self):
        text = self.text
        if text and isinstance(text, str) and len(text) > 0:
            demo = MDemo()
            demo.text = text
            demo.save()
            self.write(f"text saved successfully!")
        else:
            self.write("text is empty!")


class Delete(RequestHandler):
    # class Delete(Api):
    @property
    def id(self):
        id = self.get_argument("id", default=-1)
        return int(id)

    def get(self):
        id = self.id
        if id >= 0 and MDemo.objects.filter(id=id).exists():
            demo = MDemo.objects.filter(id=id).first()
            demo.delete()
            self.write("demo deleted successfully!")
        else:
            self.write("demo not found!")


class Update(RequestHandler):
    # class Update(Api):
    @property
    def id(self):
        id = self.get_argument("id", default=-1)
        return int(id)

    @property
    def text(self):
        text = self.get_argument("text", default="")
        return text

    def get(self):
        id = self.id
        text = self.text
        demo = MDemo.objects.filter(id=id).first()
        if demo:
            demo.text = text
            demo.save()
            self.write("demo updated successfully!")
        else:
            self.write("demo not found!")
