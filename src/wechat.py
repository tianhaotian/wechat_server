#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop

from tornado.options import define,options
from util.walk_modules import walk_modules
from handler.main_handler import main_handler
from handler.verify_handler import verify_handler
from handler.info_handler import info_handler

p = sys.argv[1]
define("port", default=p, type=int)


class Main_Application(tornado.web.Application):

    def __init__(self):
        self.handlers = self.init_handler()
        tornado.web.Application.__init__(self, handlers=self.handlers)

    def init_handler(self):
        handlers = []
        mods = walk_modules('handler')
        for mod in mods:
            if hasattr(mod, '__path__'):
                continue
            for key, cls in vars(mod).items():
                if hasattr(cls, 'ROUTE'):
                    handler = (cls.ROUTE, cls)
                    handlers.append(handler)
                    break
        return handlers

handlers = [
    (r"/", main_handler),
    (r"/api/verify", verify_handler),
    (r"/api/info", info_handler),
]

template_path = os.path.join(os.path.dirname(__file__), "template")

if __name__ == "__main__":

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers, template_path)
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()