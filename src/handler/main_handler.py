#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class main_handler(tornado.web.RequestHandler):
    '''
    Verify Server
    '''
    ROUTE = '/'

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.render("index.html")
