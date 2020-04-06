
import lib.Init as Init
from jinja2 import Template
import lib.HTTPRequest as HTTPRequest

class Commands():
    def __init__(self,environ):
        self.environ=environ


    def commands_list(self):

        http_request=HTTPRequest.HTTPRequest()
        request_get=http_request.parse_uri(self.environ['REQUEST_URI'])

        init=Init.Init()
        if 'cpe_id' in request_get:
            cpe=init.mysql.getCPEbyID(request_get['cpe_id'])
        else:
            layout_templater = open("../views/error.html").read()
            templater=Template(layout_templater)
            response=templater.render(message="CPE ID not found")
            return response

        layout_templater = open("../views/commands.html").read()
        templater=Template(layout_templater)
        commands=init.mysql.getCommandsByCpeID(request_get['cpe_id'])
        response=templater.render(cpe=cpe,commands=commands)
        return response


