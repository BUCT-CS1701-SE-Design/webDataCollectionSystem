# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum30Spider(scrapy.Spider):
    name = 'museum30'
    allowed_domains = ['dlmodernmuseum.com']
    start_urls = ['https://www.dlmodernmuseum.com/#page4']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 30
        item["museumName"] = '大连现代博物馆'
        item["Location"] = response.xpath("//i[@class='adress']/following-sibling::*/text()").extract_first().strip()
        item["Link"] = 'https://www.dlmodernmuseum.com'
        a = response.xpath(
            "//div[@class='section4-cg']/div[@class='introduce']/text()").extract()
        a = "".join(a).strip()
        opentime = a.split()
        opentime = "".join(opentime).strip()
        item["opentime"] = opentime
        item["telephone"] = '0411-84801052'
        url = 'https://www.dlmodernmuseum.com/aboutus/'
        # 处理详情页
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item": item}  # 传递参数
        )

    def parse_detail(self, response):
        item = response.meta["item"]
        content = response.xpath(
            "//div[@class='contright contrightlist rh30']/p/text()").extract_first()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
