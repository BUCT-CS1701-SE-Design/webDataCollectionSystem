# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum38Spider(scrapy.Spider):
    name = 'museum38'
    allowed_domains = ['dqsbwg.com']
    start_urls = ['http://www.dqsbwg.com/about.asp?fileid=5']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 38
        item["museumName"] = '大庆博物馆'
        item["Location"] = '大庆萨尔图区'
        item["Link"] = 'http://www.dqsbwg.com'
        item["opentime"] = '09:00—16:30(16:00停止入馆，周二闭馆)'
        item["telephone"] = '0459-4617331'
        content = response.xpath(
            "//div[@class='Section0']//font/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
