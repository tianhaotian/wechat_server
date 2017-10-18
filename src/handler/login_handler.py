#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class login_handler(tornado.web.RequestHandler):
    '''
    Verify Server
    '''
    ROUTE = '/'

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.write("success")
        self.finish()
