#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


class oauth_handler(tornado.web.RequestHandler):
    '''
    Verify Server
    '''
    ROUTE = '/api/oauth'

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        code = self.get_argument('code', '')
        self.write(code)
        self.finish()

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        code = self.get_argument('code', '')
        self.write(code)
        self.finish()