# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum28Spider(scrapy.Spider):
    name = 'museum28'
    allowed_domains = ['lvshunmuseum.org']
    start_urls = ['http://www.lvshunmuseum.org']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 28
        item["museumName"] = '旅顺博物馆'
        location = response.xpath(
            "//div[@class='body_left']/div[@class='guide']/p[last()]/text()").extract()
        del location[0]
        location = "".join(location).strip()
        item["Location"] = location
        item["Link"] = 'http://www.lvshunmuseum.org'
        opentime = response.xpath(
            "//div[@class='guide']/p[@class='p2']/text()").extract()
        opentime += response.xpath(
            "//div[@class='guide']/p[@class='p3'][position()<11]/text()").extract()
        opentime = "".join(opentime).strip()
        item["opentime"] = opentime
        telephone = response.xpath(
            "//div[@class='headbox clear']/div[@class='headtext']/p/text()").extract()
        telephone = "".join(telephone).strip()
        item["telephone"] = telephone
        url = 'http://www.lvshunmuseum.org/Aboutus/?ID=2'
        # 处理详情页
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={'item': copy.deepcopy(item)}  # 传递参数
        )

    def parse_detail(self, response):
        item = response.meta["item"]
        content = response.xpath(
            "////div[@class='abstract']/p/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
