# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    room_link = scrapy.Field()
    image_src = scrapy.Field()
    nick_name = scrapy.Field()
    city = scrapy.Field()
    image_path = scrapy.Field()
    # 爬取的时间
    utc_time = scrapy.Field()
    source = scrapy.Field()

