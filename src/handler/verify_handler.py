#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from util.WXBizMsgCrypt import WXBizMsgCrypt
import xml.etree.cElementTree as ET


class verify_handler(tornado.web.RequestHandler):
    '''
    Verify Server
    '''
    ROUTE = '/api/verify'

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.do_action()

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self, *args, **kwargs):
        self.do_post_action()

    def do_action(self):
        msg_signature = self.get_argument('msg_signature', '')
        timestamp = self.get_argument('timestamp', '')
        nonce = self.get_argument('nonce', '')
        echostr = self.get_argument('echostr', '')
        wxmsg_crypt = WXBizMsgCrypt(
            sToken='FIMcpV',
            sEncodingAESKey='2Cp1DJwT5rvp4MH4CLo4aDqiXrERKWjLWfOcPDWstAM',
            sCorpId='wwec73722ca98c0f78'
        )
        ret, sReplyEchoStr = wxmsg_crypt.VerifyURL(msg_signature, timestamp, nonce, echostr)
        self.write(sReplyEchoStr)
        self.finish()

    def do_post_action(self):
        msg_signature = self.get_argument('msg_signature', '')
        timestamp = self.get_argument('timestamp', '')
        nonce = self.get_argument('nonce', '')
        xml = self.request.body
        wxmsg_crypt = WXBizMsgCrypt(
            sToken='FIMcpV',
            sEncodingAESKey='2Cp1DJwT5rvp4MH4CLo4aDqiXrERKWjLWfOcPDWstAM',
            sCorpId='wwec73722ca98c0f78'
        )
        ret, xml_content = wxmsg_crypt.DecryptMsg(xml, msg_signature, timestamp, nonce)
        xml_tree = ET.fromstring(xml_content)
        content = xml_tree.find("Content").text
        print content
        self.write(content)
        self.finish()

