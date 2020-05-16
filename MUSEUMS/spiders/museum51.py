# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum51Spider(scrapy.Spider):
    name = 'museum51'
    allowed_domains = ['zhejiangmuseum.com']
    start_urls = ['http://www.zhejiangmuseum.com/zjbwg/ZPMbrief/about.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 51
        item["museumName"] = '浙江省博物馆'
        item["Location"] = '武林馆区地址：中山北路西湖文化广场e区29号; 孤山馆区地址：杭州市西湖区孤山路25号'
        item["Link"] = 'http://www.zhejiangmuseum.com'
        item["opentime"] = '周二至周日9:00—17:00，16:30观众停止入场，16:50开始清场'
        item["telephone"] = '0571-87960505（孤山馆区）；0571-85391628（武林馆区）'
        content = response.xpath("///html/body/div[3]/div[1]/div[3]/div/p[1]/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
