#!/usr/bin/python3
# -*- coding: utf-8 -*-

#uwsgi --socket=0.0.0.0:9201 --plugin python3 --wsgi-file ./index.py --log-to /nb/log/uwsgi.log

import sys
sys.path.append('../')

import lib.Init as Init
from jinja2 import Template
import controllers.Routing as Routing


def application(environ, start_response):

    init=Init.Init()
    init.config_file='../etc/gui.conf'
    init.read_config()

    init.mysql.connected(init.config['MYSQL']['host'],init.config['MYSQL']['port'],init.config['MYSQL']['database'],init.config['MYSQL']['user'],init.config['MYSQL']['password'])
    controller_response=""
    if 'PATH_INFO' in environ:
        routing=Routing.Routing(environ)
        controller_response=routing.run()

        # ответ при запросах ajax
        if environ['PATH_INFO'].find("ajax")>0:
            start_response('200 OK', [('Content-Type', 'text/html')])
            return [controller_response.encode()]

    else:
        controller_response=""
    
    if routing.redirect!=None:
        start_response('301 Moved Permanently', [('Location',routing.redirect)])
        return [b""]


    start_response('200 OK', [('Content-Type', 'text/html')])
    layout_templater = open("../views/layout.html").read()
    templater=Template(layout_templater)
    main_response=templater.render(controller_response=controller_response,env="")
    return [main_response.encode()]
