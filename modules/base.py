from config import constants
import requests
import json

class Base(object):

    @classmethod
    def get_url(self,endpoint):
        return constants.BASE_URL+ endpoint

    @classmethod
    def post_req(cls,end_point="",data="",headers=""):
        r = requests.post(url = cls.get_url(end_point), json = data,headers=headers)
        return json.loads(r.text)

    @classmethod
    def get_req(cls,end_point,data="",headers=""):
        r = requests.get(url = cls.get_url(end_point))
        return json.loads(r.text)


    @classmethod
    def delete_req(cls):
        pass

    @classmethod
    def update_req(cls):
        pass

    @classmethod
    def get_status(cls):
        pass

    @classmethod
    def get_message(cls):
        pass


