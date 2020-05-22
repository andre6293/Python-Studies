# -*- coding: utf-8 -*-
import scrapy


class CrawlerAtivosSpider(scrapy.Spider):
    name = 'Crawler_Ativos'
    # start_urls = [
    #     'http://https://www.investing.com/equities/StocksFilter?index_id=17920/',
    #     'https://www.investing.com/equities/StocksFilter?index_id=20'
    #     ]
    start_urls = [
        'http://https://www.investing.com/equities/StocksFilter?index_id=17920/'
        ]

    def parse(self, response):
        body_sel = scrapy.Selector(response)
        name = body_sel.xpath("//td[2]//text()").extract()
        last_rs = body_sel.xpath("//td[3]//text()").extract()
        high_rs = body_sel.xpath("//td[4]//text()").extract()
        low_rs = body_sel.xpath("//td[5]//text()").extract()
        chg = body_sel.xpath("//td[6]//text()").extract()
        chg_percent = body_sel.xpath("//td[7]//text()").extract()
        vol = body_sel.xpath("//td[8]//text()").extract()
        time = body_sel.xpath("//td[9]//text()").extract()

        for item in name:
            print(item)



# scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36" "https://www.investing.com/equities/StocksFilter?index_id=17920"