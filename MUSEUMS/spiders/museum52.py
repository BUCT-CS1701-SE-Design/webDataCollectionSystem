# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum52Spider(scrapy.Spider):
    name = 'museum52'
    allowed_domains = ['wzmuseum.cn']
    start_urls = ['http://www.wzmuseum.cn/Col/Col7/Index.aspx']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 52
        item["museumName"] = '温州博物馆'
        item["Location"] = '浙江省温州市市府路'
        item["Link"] = 'http://www.wzmuseum.cn'
        item["opentime"] = '09:00—17:00(16:00停止入馆，周一闭馆) '
        item["telephone"] = '0577-56988280'
        content = response.xpath("//div[@class='wbintro-container']//p/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
