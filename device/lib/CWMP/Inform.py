
import lib.Init as Init
import lib.DeviceDataModel as DeviceDataModel
from jinja2 import Template
import lib.HTTPTransport as HTTPTransport


class Inform():
    def __init__(self):
        pass

    def send(self):
        init=Init.Init()
        inform_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_inform']).read()
        templater=Template(inform_str)
        deviceDataModel=DeviceDataModel.DeviceDataModel()
        inform_str_parse=templater.render(params=deviceDataModel.model_data,cwmp_id=1,event='1 BOOT',date='2014-10-29T16:24:21+00:00',param_tr69_interface="none")
        http=HTTPTransport.HTTPTransport()
        return http.send(inform_str_parse)

#        print (response.content)
#        print (response.headers)        

    def sendEmpty(self):
        http=HTTPTransport.HTTPTransport()
        return http.send("")
