#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Author: jonyqin
# Created Time: Thu 11 Sep 2014 03:55:41 PM CST
# File Name: Sample.py
# Description: WXBizMsgCrypt 使用demo文件
#########################################################################
from WXBizMsgCrypt import WXBizMsgCrypt
import xml.etree.cElementTree as ET
import sys

if __name__ == "__main__":
    # 假设企业在企业微信后台上设置的参数如下
    sToken = "FIMcpV"
    sEncodingAESKey = "2Cp1DJwT5rvp4MH4CLo4aDqiXrERKWjLWfOcPDWstAM"
    # sCorpID = "tj03f873b41d2161e6"
    sCorpID = "wwec73722ca98c0f78"
    '''
     ------------使用示例一：验证回调URL---------------
     *企业开启回调模式时，企业号会向验证url发送一个get请求 
     假设点击验证时，企业收到类似请求：
     * GET /cgi-bin/wxpush?msg_signature=5c45ff5e21c57e6ad56bac8758b79b1d9ac89fd3&timestamp=1409659589&nonce=263014780&echostr=P9nAzCzyDtyTWESHep1vC5X9xho%2FqYX3Zpb4yKa9SKld1DsH3Iyt3tP3zNdtp%2B4RPcs8TgAE7OaBO%2BFZXvnaqQ%3D%3D 
     * HTTP/1.1 Host: qy.weixin.qq.com
 
     接收到该请求时，企业应	1.解析出Get请求的参数，包括消息体签名(msg_signature)，时间戳(timestamp)，随机数字串(nonce)以及企业微信推送过来的随机加密字符串(echostr),
     这一步注意作URL解码。
     2.验证消息体签名的正确性 
     3. 解密出echostr原文，将原文当作Get请求的response，返回给企业微信
     第2，3步可以用企业微信提供的库函数VerifyURL来实现。
    '''
    wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)

    '''
    ------------使用示例二：对用户回复的消息解密---------------
    用户回复消息或者点击事件响应时，企业会收到回调消息，此消息是经过企业微信加密之后的密文以post形式发送给企业，密文格式请参考官方文档
    假设企业收到企业微信的回调消息如下：
    POST /cgi-bin/wxpush? msg_signature=477715d11cdb4164915debcba66cb864d751f3e6&timestamp=1409659813&nonce=1372623149 HTTP/1.1
    Host: qy.weixin.qq.com
    Content-Length: 613
    <xml> <ToUserName><![CDATA[wx5823bf96d3bd56c7]]></ToUserName><Encrypt><![CDATA[RypEvHKD8QQKFhvQ6QleEB4J58tiPdvo+rtK1I9qca6aM/wvqnLSV5zEPeusUiX5L5X/0lWfrf0QADHHhGd3QczcdCUpj911L3vg3W/sYYvuJTs3TUUkSUXxaccAS0qhxchrRYt66wiSpGLYL42aM6A8dTT+6k4aSknmPj48kzJs8qLjvd4Xgpue06DOdnLxAUHzM6+kDZ+HMZfJYuR+LtwGc2hgf5gsijff0ekUNXZiqATP7PF5mZxZ3Izoun1s4zG4LUMnvw2r+KqCKIw+3IQH03v+BCA9nMELNqbSf6tiWSrXJB3LAVGUcallcrw8V2t9EL4EhzJWrQUax5wLVMNS0+rUPA3k22Ncx4XXZS9o0MBH27Bo6BpNelZpS+/uh9KsNlY6bHCmJU9p8g7m3fVKn28H3KDYA5Pl/T8Z1ptDAVe0lXdQ2YoyyH2uyPIGHBZZIs2pDBS8R07+qN+E7Q==]]></Encrypt>
    <AgentID><![CDATA[218]]></AgentID>
    </xml>
 
    企业收到post请求之后应该 1.解析出url上的参数，包括消息体签名(msg_signature)，时间戳(timestamp)以及随机数字串(nonce)
    2.验证消息体签名的正确性。 3.将post请求的数据进行xml解析，并将<Encrypt>标签的内容进行解密，解密出来的明文即是用户回复消息的明文，明文格式请参考官方文档
    第2，3步可以用企业微信提供的库函数DecryptMsg来实现。
    '''
    sReqMsgSig = "6573d07dd2927db9e64e80904fc30789dc5bfbed"
    sReqTimeStamp = "1508140545"
    sReqNonce = "938344070"
    sReqData = '''<xml><ToUserName><![CDATA[wwec73722ca98c0f78]]></ToUserName>
<Encrypt><![CDATA[ciRO7Fgac9CIVwmj6hIoBlVQJ1U+x85evW+ZM/groyEgD8tIw+eH4kShGMeeApWhU/K0zbNYpv/NEs/ay+V6xbSQhI1ICNFOsC4PRrZgKQV14JiA+BRakQUrL8s9BblwJGkgnS/EI/htvpteyfAWEEbdwifzL85I5VOv+IRW6xrNbEx5PV/tHrFSoIUW3vskKEhVaA1yFE3gnzA7OT8mZBCho3oynr7gY7trybjgSv4iXqmraX3RcPOwkVxtkZRT1B9RqybdkhvvXGHrHikxdw+W/OLmAiwNz5i5QQRUDN3LP5RWKHbHMxyJEpAqHnp+UxwDyv9DinhH3iCtwHHD1VMOPze27zCfy1fJZ7q3BwkEzqst16IzlVZvhyJb4iQGRXgTcq46wAoItkjSj6jouLZ+xM3wZywPVBW8YOCJBYQ=]]></Encrypt>
<AgentID><![CDATA[1000008]]></AgentID>
</xml>'''
    ret, sMsg = wxcpt.DecryptMsg(sReqData, sReqMsgSig, sReqTimeStamp, sReqNonce)
    print ret, sMsg
    if (ret != 0):
        print "ERR: DecryptMsg ret: " + str(ret)
        sys.exit(1)
    # 解密成功，sMsg即为xml格式的明文
    # TODO: 对明文的处理
    # For example:
    xml_tree = ET.fromstring(sMsg)
    content = xml_tree.find("Content").text
    print content
    # ...
    # ...

    '''
    ------------使用示例三：企业回复用户消息的加密---------------
    企业被动回复用户的消息也需要进行加密，并且拼接成密文格式的xml串。
    假设企业需要回复用户的明文如下：
    <xml>
    <ToUserName><![CDATA[mycreate]]></ToUserName>
    <FromUserName><![CDATA[wx5823bf96d3bd56c7]]></FromUserName>
    <CreateTime>1348831860</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[this is a test]]></Content>
    <MsgId>1234567890123456</MsgId>
    <AgentID>128</AgentID>
    </xml>
 
    为了将此段明文回复给用户，企业应： 1.自己生成时间时间戳(timestamp),随机数字串(nonce)以便生成消息体签名，也可以直接用从企业微信的post url上解析出的对应值。
    2.将明文加密得到密文。   3.用密文，步骤1生成的timestamp,nonce和企业在企业微信设定的token生成消息体签名。   4.将密文，消息体签名，时间戳，随机数字串拼接成xml格式的字符串，发送给企业号。
    以上2，3，4步可以用企业微信提供的库函数EncryptMsg来实现。
    '''
    sRespData = "<xml><ToUserName>ww1436e0e65a779aee</ToUserName><FromUserName>ChenJiaShun</FromUserName><CreateTime>1476422779</CreateTime><MsgType>text</MsgType><Content>你好</Content><MsgId>1456453720</MsgId><AgentID>1000002</AgentID></xml>"
    ret, sEncryptMsg = wxcpt.EncryptMsg(sRespData, sReqNonce, sReqTimeStamp)
    if (ret != 0):
        print "ERR: EncryptMsg ret: " + str(ret)
        sys.exit(1)
        # ret == 0 加密成功，企业需要将sEncryptMsg返回给企业号
        # TODO:
        # HttpUitls.SetResponse(sEncryptMsg)
