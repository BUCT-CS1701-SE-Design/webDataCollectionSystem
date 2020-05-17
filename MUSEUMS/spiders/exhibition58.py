# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item


class Exhibition58Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition58'
    allowed_domains = ['hzwhbwg.com']
    start_urls = ['http://www.hzwhbwg.com/index.php/list-11-1.html']

    def parse(self, response):
        li_list=response.xpath("//div[@class='exhibition']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=58
            item["exhibitionTheme"]=li.xpath("./a/div[@class='exhmain']/h5/text()").extract_first()
            item["exhibition_picture"]='http://www.hzwhbwg.com'+li.xpath("./a/div[1]/img/@src").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./a/div[@class='exhmain']/p/text()").extract_first()
            item["exhibitionTime"]=''
            yield item