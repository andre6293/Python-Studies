# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerAcoesItem(scrapy.Item):
    name = scrapy.Field()
    last_rs = scrapy.Field()
    high_rs = scrapy.Field()
    low_rs = scrapy.Field()
    chg = scrapy.Field()
    chg_percent = scrapy.Field()
    vol = scrapy.Field()
    time = scrapy.Field()
