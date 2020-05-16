# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum47Spider(scrapy.Spider):
    name = 'museum47'
    allowed_domains = ['szmuseum.com']
    start_urls = ['http://www.szmuseum.com/News/Index/GZZC']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 47
        item["museumName"] = '苏州博物馆'
        item["Location"] = '苏州市东北街204号'
        item["Link"] = 'http://www.szmuseum.com'
        item["opentime"] = '每星期二至星期日9:00-17:00（16:00停止入馆），每星期一闭馆（国家法定节假日除外）'
        item["telephone"] = '0512-67575666'
        content = response.xpath("//*[@id='divContent']/p[3]/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
