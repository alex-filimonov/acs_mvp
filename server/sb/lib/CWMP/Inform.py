
import lib.Init as Init
from jinja2 import Template
import secrets


class Inform():
    def __init__(self,request):
        self.request=request
        self.body_response=""
        self.coockie_response=""


    def generateSessionID(self):
        return secrets.token_urlsafe(36)  

    def InformResponse(self):
        init=Init.Init()
        inform_str = open(init.config['TEMPLATERS']['templater_dir']+'/'+init.config['TEMPLATERS']['templater_inform_response']).read()
        templater=Template(inform_str)
        self.request.CWMP_ID=int(int(self.request.CWMP_ID)+1)
        inform_str_parse=templater.render(cwmp_id=self.request.CWMP_ID)

        serial_number=None
        vendor_name=None
        model_name=None

        if 'SOAP-ENV:Envelope' in self.request.request_dict:
            if 'SOAP-ENV:Body' in self.request.request_dict['SOAP-ENV:Envelope']:
                if 'cwmp:Inform' in self.request.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']:
                    if 'DeviceId' in self.request.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['cwmp:Inform']:
                        if 'SerialNumber' in self.request.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['cwmp:Inform']['DeviceId']:
                            serial_number=self.request.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['cwmp:Inform']['DeviceId']['SerialNumber']
                        if 'Manufacturer' in self.request.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['cwmp:Inform']['DeviceId']:
                            vendor_name=self.request.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['cwmp:Inform']['DeviceId']['Manufacturer']
                        if 'OUI' in self.request.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['cwmp:Inform']['DeviceId']:
                            model_name=self.request.request_dict['SOAP-ENV:Envelope']['SOAP-ENV:Body']['cwmp:Inform']['DeviceId']['OUI']

        if serial_number==None:
            self.body_response=""
            self.coockie_response=""
            return

        coockie_session_id="tr69-"+self.generateSessionID()
        init.redis.write(coockie_session_id+":serial_number",serial_number)
        init.redis.write(coockie_session_id+":command","InformResponse")

        cpe=init.mysql.getCPEbySN(serial_number)
        if (cpe==None):
            init.mysql.insertCPE(serial_number,vendor_name,model_name,self.request.request_body)
        else:
            init.mysql.updateCPE(cpe['id'],vendor_name,model_name,self.request.request_body)

        self.body_response=inform_str_parse
        self.coockie_response="session_id="+coockie_session_id


