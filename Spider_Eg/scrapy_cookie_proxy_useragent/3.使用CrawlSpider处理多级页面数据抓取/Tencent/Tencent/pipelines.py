# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from datetime import datetime
from Tencent.items import TencentItem, PositionItem

class TencentPipeline(object):
    def open_spider(self, spider):
        self.f = open("tencent.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            item["utcnow"] = str(datetime.utcnow())
            item["source"] = spider.name

            content = json.dumps(dict(item)) + ",\n"
            self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()

class PositionPipeline(object):
    def open_spider(self, spider):
        self.f = open("position.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, PositionItem):
            item["utcnow"] = str(datetime.utcnow())
            item["source"] = spider.name

            content = json.dumps(dict(item)) + ",\n"
            self.f.write(content)
        return item

    def close_spider(self, spider):
        self.f.close()
