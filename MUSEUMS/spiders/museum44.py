# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum44Spider(scrapy.Spider):
    name = 'museum44'
    allowed_domains = ['njmuseum.com']
    start_urls = ['http://www.njmuseum.com/zh/articleDetails?id=9064']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 44
        item["museumName"] = '南京博物院'
        item["Location"] = '南京市中山东路321号'
        item["Link"] = 'http://www.njmuseum.com'
        item["opentime"] = '周二-周日：9:00-17:00 16:00停止检票'
        item["telephone"] = '025-84807923'
        item["introduction"] = '南京博物院坐落于南京市紫金山南麓、中山门内北侧，占地70000余平方米，是我国第一座由国家投资兴建的大型综合类博物馆。被评为“全国公共文化设施管理先进单位”、“国家一级博物馆”、“中央地方共建国家级博物馆”、“全国爱国主义教育示范基地”。'
        print(item)
        yield item
