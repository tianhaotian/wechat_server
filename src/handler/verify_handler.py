#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import uuid

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

    def get(self):
        self.do_action()

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self, *args, **kwargs):
        self.do_action()

    def do_action(self):
        if self.request.body:

            print "there is post body"

            self.write('ok')
            self.finish()
        else:
            self.write('fail')
            self.finish()



