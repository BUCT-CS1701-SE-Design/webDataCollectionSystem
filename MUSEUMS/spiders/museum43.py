# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum43Spider(scrapy.Spider):
    name = 'museum43'
    allowed_domains = ['cyjng.net']
    start_urls = ['http://www.cyjng.net/Default.aspx?tabid=70&language=zh-CN']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 43
        item["museumName"] = '上海鲁迅纪念馆'
        item["Location"] = '上海市青浦区练塘镇朱枫公路3516号'
        item["Link"] = 'http://www.cyjng.net'
        item["opentime"] = '周二-周日：9:00-16:00，15:00停止领票，周一闭馆'
        item["telephone"] = '021-59257178'
        content = response.xpath("//*[@id='dnn_ctr502_HtmlModule_HtmlModule_lblContent']/p[2]/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
