# -*- coding: utf-8 -*-
import scrapy


class TesteCrawlSpider(scrapy.Spider):
    name = 'teste_crawl'
    allowed_domains = ['https://blog.scrapinghub.com/page/1/']
    start_urls = ['https://blog.scrapinghub.com/page/1/']

    def parse(self, response):
        page = response.url.split('/')[-1]
        with open('teste.html', 'wb') as f:
            f.write(response.body)