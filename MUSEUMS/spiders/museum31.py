# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum31Spider(scrapy.Spider):
    name = 'museum31'
    allowed_domains = ['museum.nenu.edu.cn']
    start_urls = ['http://museum.nenu.edu.cn/bggk/cgzn.htm']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 31
        item["museumName"] = '吉林省自然博物馆'
        item["Location"] = '吉林省长春市净月大街2556号东北师范大学自然博物馆'
        item["Link"] = 'http://museum.nenu.edu.cn'
        a = response.xpath(
            "//div[@id='vsb_content']/p[position()=2]/text()").extract()
        a = "".join(a).strip()
        b = response.xpath(
            "//div[@id='vsb_content']/p[position()=3]/text()").extract()
        b = "".join(b).strip()
        item["opentime"] = a+b
        item["telephone"] = '0431-84537568'
        url = 'http://museum.nenu.edu.cn/'
        # 处理详情页
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={'item': copy.deepcopy(item)}  # 传递参数
        )

    def parse_detail(self, response):
        item = response.meta["item"]
        content = response.xpath(
            "//div[@class='leader']/p/font/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
