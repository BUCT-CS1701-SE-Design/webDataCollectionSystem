# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum34Spider(scrapy.Spider):
    name = 'museum34'
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%9C%E5%8C%97%E7%83%88%E5%A3%AB%E7%BA%AA%E5%BF%B5%E9%A6%86/2977069?fr=aladdin']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 34
        item["museumName"] = '东北烈士纪念馆'
        item["Location"] = '哈尔滨市南岗区一曼街241号'
        item["Link"] = 'http://www.jn1948.cn'
        item["opentime"] = '9:00-16:00'
        item["telephone"] = '0451—53643712 / 0451—53640948'
        content = response.xpath("/html/body/div[3]/div[2]/div/div[2]/div[14]/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
