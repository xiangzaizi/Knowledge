#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2

def send_request():
    # 发送请求的url是通过抓包找到的
    base_url = "https://movie.douban.com/j/chart/top_list?"
    # 查询字符串参数，也是通过抓包找到的
    query_data = {"type" : "24",
        "interval_id" : "100:90",
        "action" : "",
        "start" : "0",
        "limit" : "20"
    }

    query_str = urllib.urlencode(query_data)
    full_url = base_url + query_str
    print full_url

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    request = urllib2.Request(full_url, headers = headers)

    response = urllib2.urlopen(request)
    html = response.read()

    return html

if __name__ == "__main__":
    html = send_request()
    print html
