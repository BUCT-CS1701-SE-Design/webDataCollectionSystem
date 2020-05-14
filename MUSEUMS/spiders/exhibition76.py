# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }

class Exhibition76Spider(scrapy.Spider):
    name = 'exhibition76'
    allowed_domains = ['hnzzmuseum.com']
    start_urls = ['http://www.hnzzmuseum.com/display10_list1.html']
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=76
        d_list=response.xpath("//div[@class='special_box']/div[@class='special_list']")
        for d in d_list:
            item["exhibitionTheme"]=d.xpath("./ul/li/a/p[1]/text()").extract_first()
            item["exhibition_picture"]='http://www.hnzzmuseum.com'+d.xpath("./ul/img/@src").extract_first()
            content=d.xpath("./ul/li/a/p[@class='special_c']/span/text()").extract()
            item["exhibitionIntroduction"]=''.join(content)
            #print(item)
            item["exhibitionTime"]=''
            yield item
            #print(item)