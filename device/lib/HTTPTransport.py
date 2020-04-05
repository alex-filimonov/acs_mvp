
import requests
import lib.Init as Init
import xmltodict
import pprint
import json


class HTTPTransport():
    def __init__(self):
        self.response_dict=None
        self.response_str=None

    def send(self,str_data):
        init=Init.Init()
        headers ={
            'Content-Type': 'text/xml',
            'Accept': 'application/xml',
        }
        if (init.coockie!=None):
            headers['Cookie']=init.coockie

        response = requests.request("POST", init.get_acs_url(), headers = headers, data = str_data)
        self.response_str=response.content
        if (len(self.response_str)>1):
            self.response_dict = xmltodict.parse(self.response_str)
        else:
            self.response_dict={}

        if 'Set-Cookie' in response.headers:
            init.coockie=response.headers['Set-Cookie']

        return self.response_dict
        