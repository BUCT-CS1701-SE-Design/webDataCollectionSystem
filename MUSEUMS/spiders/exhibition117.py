# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition117Spider(scrapy.Spider):
    name = 'exhibition117'
    allowed_domains = ['hylae.com']
    start_urls = ['http://www.hylae.com/index.php?ac=article&at=list&tid=33']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=117
        li_list=response.xpath("/html//div[3]/div[3]/ul/li")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("./span[2]/a/text()").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./span[3]/text()").extract_first()
            item["exhibition_picture"]='http://www.hylae.com/'+li.xpath("./span[1]/a/img/@src").extract_first()
            yield item
        