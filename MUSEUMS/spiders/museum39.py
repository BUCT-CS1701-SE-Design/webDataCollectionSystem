# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum39Spider(scrapy.Spider):
    name = 'museum39'
    allowed_domains = ['shanghaimuseum.net']
    start_urls = ['https://www.shanghaimuseum.net/museum/frontend/infomation/introduction.action']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 39
        item["museumName"] = '上海博物馆'
        item["Location"] = '上海市黄浦区人民大道201号'
        item["Link"] = 'https://www.shanghaimuseum.net'
        item["opentime"] = '9:00—17:00 16:00后停止入场（每周一闭馆，除国定假日外）'
        item["telephone"] = '021-63723500'
        item["introduction"] = response.xpath(
            "//div[@class='clearfix']/p/text()").extract_first()
        yield item
