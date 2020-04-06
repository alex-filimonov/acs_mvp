
import lib.Init as Init
from jinja2 import Template
import lib.HTTPRequest as HTTPRequest


class CPE():
    def __init__(self,environ):
        self.environ=environ

    def index(self):
        
        init=Init.Init()
        cpes=init.mysql.getAllCPE()
        layout_templater = open("../views/cpe_list.html").read()
        templater=Template(layout_templater)
        response=templater.render(cpes=cpes)
        return response


    def ajax_cpe_inform(self):
        http_request=HTTPRequest.HTTPRequest()
        request_get=http_request.parse_uri(self.environ['REQUEST_URI'])

        init=Init.Init()
        cpes=init.mysql.getCPEbyID(request_get['cpe_id'])
        return cpes["all_inform"]
