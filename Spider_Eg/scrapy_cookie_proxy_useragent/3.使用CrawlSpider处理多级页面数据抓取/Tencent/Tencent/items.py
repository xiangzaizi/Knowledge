# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    """
        存储职位列表页数据
    """
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    people_number = scrapy.Field()
    work_location = scrapy.Field()
    publish_times = scrapy.Field()
    # 记录抓取时间
    utcnow = scrapy.Field()
    # 记录数据源
    source = scrapy.Field()

class PositionItem(scrapy.Item):
    """
        存储职位详情页数据
    """
    position_link = scrapy.Field()
    # 工作职责
    position_zhize = scrapy.Field()
    # 工作要求
    position_yaoqiu = scrapy.Field()
    # 记录抓取时间
    utcnow = scrapy.Field()
    # 记录数据源
    source = scrapy.Field()

