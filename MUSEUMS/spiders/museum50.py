# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum50Spider(scrapy.Spider):
    name = 'museum50'
    allowed_domains = ['njmuseumadmin.com']
    start_urls = ['http://www.njmuseumadmin.com/About/show/id/43']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 50
        item["museumName"] = '南京市博物总馆'
        item["Location"] = '南京市秦淮区朝天宫4号'
        item["Link"] = 'http://www.njmuseumadmin.com'
        item["opentime"] = '9:00—18:00（周一闭馆）'
        item["telephone"] = '025-84217123'
        content = response.xpath(
            "//div[@class='intro_con']/p/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        print(item)
        yield item
