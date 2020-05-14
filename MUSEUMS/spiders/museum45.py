# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum45Spider(scrapy.Spider):
    name = 'museum45'
    allowed_domains = ['19371213.com.cn']
    start_urls = ['http://www.19371213.com.cn/about/museum/201608/t20160827_5907664.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 45
        item["museumName"] = '侵华日军南京大屠杀遇难同胞纪念馆'
        item["Location"] = '南京市水西门大街418号'
        item["Link"] = 'http://www.19371213.com.cn'
        item["opentime"] = '8:30—16:30 （17:30闭馆） 周二至周日，周一闭馆（国家法定节假日除外）'
        item["telephone"] = '86-018013959265'
        content = response.xpath("//p/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
