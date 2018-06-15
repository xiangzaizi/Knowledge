# -*- coding:utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
from gevent import monkey
monkey.patch_all()
import gevent
import time
import csv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TencentSpider(object):
    def __init__(self):
        self.base_url = "https://hr.tencent.com/position.php?"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.begin_page = int(raw_input("请输入起始页:"))
        self.end_page = int(raw_input("请输入结束页:"))
        self.job_list = []

    def send_request(self, params={}):
        # 这里需要返回的内容就不要添加: content
        response = requests.get(self.base_url, params=params, headers=self.headers)
        return response

    def html_page(self, html):
        # bs4 css选择器
        soup = BeautifulSoup(html, 'lxml')
        # 解析页面内容获取, 解析职位(职位详情的跳转信息) 类别 人数  工作位置

        tr_list = soup.find_all("tr", {"class": ["odd", "even"]})

        for tr in tr_list:
            job = {}

            job["job_no"] = tr.select("td a")[0].get_text()[:5]
            job["job_name"] = tr.select("td a")[0].get_text()[6:]
            # 职位的跳转详情跳转链接
            job["job_link"] = "https://hr.tencent.com/" + tr.select("td a")[0].get("href")
            job["job_type"] = tr.select("td")[1].get_text()
            job["job_num"] = tr.select("td")[2].get_text()
            job["job_position"] = tr.select("td")[3].get_text()
            job["update_time"] = tr.select("td")[4].get_text()

            self.job_list.append(job)

    def write_page(self, job_list):
        # 将接收的内容写入json文件
        # 内容的简写
        # json_file = json.dump(job_list, open('./tencentjob.json', 'w'))

        json_file = json.dumps(job_list)  # 转成json数据格式
        return json_file

    def json_csv(self, json_file):
        # json_file = open(json_file, "r")
        #
        csv_file = open("tencent.csv", "w")

        # 读取json文件的字符串, 并返回python数据类型
        item_list = json.loads(json_file)  # 将json数据转换成python数据格式loads!!!

        # 创建一个csv文件读写操作对象, 数据读写和文件交互
        csv_writer = csv.writer(csv_file)

        # 表头一层嵌套的列表, 这一部分就是字段那一栏
        sheet_head = item_list[0].keys()
        # 表数据是两层嵌套的列表--->表单内的数据
        sheet_data = [item.values() for item in item_list]

        # 先写一行表头部分
        csv_writer.writerow(sheet_head)
        csv_writer.writerows(sheet_data)

        # 关闭文件, 保存数据
        csv_file.close()
        # json_file.close()


    def main(self):
        # 下载指定页面的职位信息数据
        for page in range(self.begin_page, self.end_page + 1):
            # 每页显示10条数据
            pn = (page - 1)*10
            # 放到url中
            # https://hr.tencent.com/position.php?$start=10
            params = {"start": pn}
            # 1. 获取请求下来的整个页面
            page_html = self.send_request(params).content


            # 2. 对页面进行解析
            self.html_page(page_html)

            # 3. 将页面内容写入json文件中
            json_file = self.write_page(self.job_list)
            # print "in work %s" % gevent.getcurrent()

            # 4.
            self.json_csv(json_file)

if __name__ == '__main__':
    spider = TencentSpider()
    spider.main()
    # TencentSpider().main()
    start = time.time()

    g1 = gevent.spawn(spider.main())
    g2 = gevent.spawn(spider.main())
    g3 = gevent.spawn(spider.main())

    gevent.joinall([g1, g2, g3])

    end = time.time()

    print end - start

