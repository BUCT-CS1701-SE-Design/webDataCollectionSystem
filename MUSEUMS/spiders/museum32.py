# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum32Spider(scrapy.Spider):
    name = 'museum32'
    allowed_domains = ['jlmuseum.org']
    start_urls = ['http://www.jlmuseum.org/description']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 32
        item["museumName"] = '吉林省博物院'
        item["Location"] = '长春净月国家高新技术产业开发区永顺路1666号'
        item["Link"] = 'http://www.jlmuseum.org'
        item["opentime"] = '每周二至周日9：30——15：30（15：00停止入馆）；每周一闭馆（国家法定节假日除外）。'
        item["telephone"] = '0431-88917353  81959582'

        content = response.xpath(
            "//div[@class='cont']/p[@style='text-align:left;text-indent:24pt;'][position()=1]/span/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
