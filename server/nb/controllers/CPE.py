
import lib.Init as Init
from jinja2 import Template

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
        init=Init.Init()
        cpes=init.mysql.getCPEbyID(7)
        return cpes["all_inform"]
