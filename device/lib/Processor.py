
import lib.CWMP.Inform as Inform
import lib.Init as Init

class Processor():
    def __init__(self):
        self.cwmp_id=1
        self.cookies=""

    def do(self):
        init=Init.Init()
        inform=Inform.Inform()
        response=inform.send()
        if 'SOAP-ENV:Envelope' in response:
            if 'soapenv:Header' in response['SOAP-ENV:Envelope']:
                if 'cwmp:ID' in response['SOAP-ENV:Envelope']['soapenv:Header']:
                    self.cwmp_id=int(response['SOAP-ENV:Envelope']['soapenv:Header']['cwmp:ID']['#text'])

        response=inform.sendEmpty()

        while (response):
            print (response)
            

        


