# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum42Spider(scrapy.Spider):
    name = 'museum42'
    allowed_domains = ['sstm.org.cn']
    start_urls = ['http://www.sstm.org.cn/about']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 42
        item["museumName"] = '上海科技馆'
        item["Location"] = '上海浦东新区世纪大道2000号'
        item["Link"] = 'http://www.sstm.org.cn'
        item["opentime"] = '9:00-17:15 周二至周日 周一休馆(黄金周除外)'
        item["telephone"] = '021-68542000'
        content = response.xpath("//meta[@name='description']/@content").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
