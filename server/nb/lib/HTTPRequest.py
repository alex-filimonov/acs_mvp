
import xmltodict
import pprint
import json


class HTTPRequest():
    def __init__(self,environ):
        self.cookies=""
        self.cookies_parse={}
        self.request_body=""
        self.request_body_size = 0
        self.request_dict={}
        self.CWMP_ID=None
        self.cwmp_methods=[]

        self.parse(environ)



    def parse(self,environ):
        try:
            self.request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            self.request_body_size = 0
        self.request_body = environ['wsgi.input'].read(self.request_body_size)
        if (len(self.request_body)>1):
            self.request_dict = xmltodict.parse(self.request_body)
        else:
            self.request_dict={}

        if 'SOAP-ENV:Envelope' in self.request_dict:
            if 'SOAP-ENV:Header' in self.request_dict['SOAP-ENV:Envelope']:
                if 'cwmp:ID' in self.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Header']:
                    if '#text' in self.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Header']['cwmp:ID']:
                        self.CWMP_ID=self.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Header']['cwmp:ID']['#text']

            if 'SOAP-ENV:Body' in self.request_dict['SOAP-ENV:Envelope']:
                for key in self.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']:
                    self.cwmp_methods.append(key)

        if 'HTTP_COOKIE' in environ:
            self.cookies=environ['HTTP_COOKIE']
            ar=self.cookies.split(',')
            for sub_coockie in ar:
                ar2=sub_coockie.split('=')
                if (len(ar2)>1):
                    self.cookies_parse[ar2[0]]=ar2[1]

        





