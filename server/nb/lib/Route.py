

import lib.CWMP.Inform as Inform
import lib.Init as Init


class Route():
    def __init__(self,request):
        self.request=request
        self.body_response=""
        self.coockie_response=""
        self.serial_number=""
        self.last_command=""

    def run(self):
        init=Init.Init()

        if 'session_id' in self.request.cookies_parse:
            # есть кук с сессией
            self.serial_number=init.redis.read(self.request.cookies_parse['session_id']+":serial_number")
            self.last_command=init.redis.read(self.request.cookies_parse['session_id']+":command")

            init.redis.write(self.request.cookies_parse['session_id']+":serial_number",self.serial_number)
            init.redis.write(self.request.cookies_parse['session_id']+":command","Empty")

            if (self.last_command==b"InformResponse"):
                #считываем задания и отправляем их, пока пусто
                print (self.request.request_body)



            self.body_response=""
            self.coockie_response='session_id='+self.request.cookies_parse['session_id']
            return 
        else:
            if (len(self.request.cwmp_methods)>0): # есть метод
                if (self.request.cwmp_methods[0]=="cwmp:Inform"):
                    inform=Inform.Inform(self.request)
                    inform.InformResponse()
                    self.body_response=inform.body_response
                    self.coockie_response=inform.coockie_response
                    return

        # в дефолте всем отлуп
        self.body_response=""
        self.coockie_response=""
        return

