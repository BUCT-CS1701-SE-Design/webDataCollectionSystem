# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum40Spider(scrapy.Spider):
    name = 'museum40'
    allowed_domains = ['luxunmuseum.cn']
    start_urls = ['http://www.luxunmuseum.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 40
        item["museumName"] = '上海鲁迅纪念馆'
        item["Location"] = '上海市虹口区甜爱路200号'
        item["Link"] = 'http://www.luxunmuseum.cn'
        item["opentime"] = '上午9：00——下午17：00（16:00停止入场，周一闭馆，国定节假日除外）'
        item["telephone"] = '86-21-65402288'
        content = response.xpath(
            "//div[@class='am-u-sm-7 ']/p/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
