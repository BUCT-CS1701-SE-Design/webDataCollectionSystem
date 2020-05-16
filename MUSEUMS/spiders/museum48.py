# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum48Spider(scrapy.Spider):
    name = 'museum48'
    allowed_domains = ['yzmuseum.com']
    start_urls = ['https://www.yzmuseum.com/website/aboutyzm/intro.php']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 48
        item["museumName"] = '扬州博物馆'
        item["Location"] = '扬州文昌西路明月湖西侧'
        item["Link"] = 'https://www.yzmuseum.com'
        item["opentime"] = '每周二至周日：9:00——17:00（16:00停止入场）'
        item["telephone"] = '(86)0514-85228003'
        content = response.xpath("//div[@id='content_body']/p/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
