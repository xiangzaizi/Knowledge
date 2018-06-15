# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from settings import USER_AGENT_LIST
import random
import base64

class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers["User-Agent"] = user_agent
        # 不需要return request，如果返回就是返回给引擎处理
        #print request.headers["User-Agent"]

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        """
        # 免费透明代理：
        proxy = "114.67.224.167:16819"
        request.meta['proxy'] = "http://" + proxy
        """
        # 验证代理使用：
        proxy = "maozhaojun:ntkn0npx@114.67.224.167:16819"
        request.meta['proxy'] =  proxy

        # 早期Scrapy中用验证代理的方法：
        """
        user_passwd = "maozhaojun:ntkn0npx"
        ip_port = "@114.67.224.167:168191"
        base64_user_passwd = base64.b64encode(user_passwd)
        request.headers['Proxy-Authorization'] = "Basic " + base64_user_passwd
        request.meta['proxy'] = "http://" + proxy
        """




