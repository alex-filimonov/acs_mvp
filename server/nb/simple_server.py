#!/usr/bin/python3
# -*- coding: utf-8 -*-

#uwsgi --http 0.0.0.0:8080 --wsgi-file ./wsgi.py
#uwsgi --http-socket 0.0.0.0:9100 --plugin python3 --wsgi-file ./symple_server.p

import sys
import lib.Init as Init
import lib.HTTPRequest as HTTPRequest
import lib.Route as Route

def application(environ, start_response):


    init=Init.Init()
    init.config_file='./etc/acs.conf'
    init.read_config()


    request=None
#    try:
    init.redis.connect(init.config['REDIS']['host'],init.config['REDIS']['port'])

    request=HTTPRequest.HTTPRequest(environ)
    route=Route.Route(request)
    route.run()
    start_response('200 OK', [('Content-Type', 'text/xml'),('Set-Cookie', route.coockie_response)])
    return [route.body_response.encode()]






