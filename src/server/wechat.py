#!/usr/bin/env python
#-*- coding:utf-8 -*-

import multiprocessing
import sys
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop

from tornado.options import define,options
from util.walk_modules import walk_modules

p = sys.argv[1]
define("port", default=p, type=int)
define("bdptag", default="enterprise", help="service tag")


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

if __name__ == "__main__":

    tornado.options.parse_command_line()
    app = Main_Application()
    httpserver = tornado.httpserver.HTTPServer(app)
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()