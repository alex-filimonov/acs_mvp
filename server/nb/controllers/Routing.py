
import controllers.CPE as CPE
import controllers.Commands as Commands

from jinja2 import Template
import lib.HTTPRequest as HTTPRequest
import sys


class Routing():
    def __init__(self,environ):
        self.environ=environ
        self.redirect=None

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

        if self.environ['PATH_INFO']=='/cpe_add_commands':
            commands=Commands.Commands(self.environ)
            commands.add_command()
            if commands.cpe_id!=None:
                self.redirect="/cpe_commands?cpe_id="+commands.cpe_id
            else:
                self.redirect="/"
            return ""

        if self.environ['PATH_INFO']=='/cpe_del_commands':
            commands=Commands.Commands(self.environ)
            commands.del_command()
            if commands.cpe_id!=None:
                self.redirect="/cpe_commands?cpe_id="+commands.cpe_id
            else:
                self.redirect="/"
            return ""

        layout_templater = open("../views/error.html").read()
        templater=Template(layout_templater)
        response=templater.render(message="Unknow route path !!!!")

        return response
