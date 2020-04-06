
import controllers.CPE as CPE
import controllers.Commands as Commands

from jinja2 import Template

class Routing():
    def __init__(self,environ):
        self.environ=environ

    def run(self):
        if self.environ['PATH_INFO']=='/':
            cpe=CPE.CPE(self.environ)
            return cpe.index()

        if self.environ['PATH_INFO']=='/cpe_inform_ajax':
            cpe=CPE.CPE(self.environ)
            return cpe.ajax_cpe_inform()

        if self.environ['PATH_INFO']=='/cpe_commands':
            commands=Commands.Commands(self.environ)
            return commands.commands_list()


        layout_templater = open("../views/error.html").read()
        templater=Template(layout_templater)
        response=templater.render(message="Unknow route path !!!!")

        return response
