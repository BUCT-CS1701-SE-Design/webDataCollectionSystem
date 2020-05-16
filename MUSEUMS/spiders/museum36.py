# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum36Spider(scrapy.Spider):
    name = 'museum36'
    allowed_domains = ['aihuihistorymuseum.org.cn']
    start_urls = ['http://www.aihuihistorymuseum.org.cn']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 36
        item["museumName"] = '瑷珲历史陈列馆'
        item["Location"] = '黑龙江省黑河市瑷珲镇萨布素街'
        item["Link"] = 'http://www.aihuihistorymuseum.org.cn'
        item["opentime"] = '开放时间：除春节三天法定假日外常年开放 （具体开闭馆时间请关注瑷珲历史陈列馆微信公众号）'
        item["telephone"] = '0456-8201907'
        content = response.xpath(
            "//div[@class='ai_about_con']/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
