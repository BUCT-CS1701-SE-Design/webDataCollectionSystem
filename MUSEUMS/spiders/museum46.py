# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum46Spider(scrapy.Spider):
    name = 'museum46'
    allowed_domains = ['ntmuseum.com']
    start_urls = ['http://www.ntmuseum.com/guide/intro/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 46
        item["museumName"] = '南通博物苑'
        item["Location"] = '南通市濠南路19号'
        item["Link"] = 'http://www.ntmuseum.com'
        item["opentime"] = '1、园林景观：全年免费开放。开放时间：春、夏季（4月1日——10月31日）5：30——18：00（17:30停止进园）。秋、冬季（11月1日——3月31日）5：30——17：00（16:30停止进园）。  2、建筑展厅：各展厅开放时间：周二至周日9：00—17：00（16:30停止入馆），周一闭馆（法定节假日除外）。'
        item["telephone"] = '0513—85516233 85062528'
        content = response.xpath("//*[@id='pub_right']/div/div/ul/li[3]/text()[1]").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
