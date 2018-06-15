#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import ssl

# 当网站的数字证书不是第三方数字证书中心颁布的，可能是自己制作伪造
# 这样的网站可以通过下面的方法访问
# 1. 忽略网站证书认证的对象
context = ssl._create_unverified_context()

def send_request():
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    #url = "https://www.baidu.com/"
    url = "https://www.12306.cn/mormhweb/"
    request = urllib2.Request(url, headers = headers)
    # 2. 添加context参数
    response = urllib2.urlopen(request, context = context)

    print response.read()

# 方式二 通过设置忽略警告的方式来忽略屏蔽
import requests
from requests.packages import urllib3

urllib3.disable_warnings()
response = requests.get(url, verfy=False)

# 方式三 通过捕获警告日志的方式忽略警告
import logging
import requests
logging.captureWarnings(True)
response = requests.get(url, verfy=False)



if __name__ == "__main__":
    send_request()
