# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition105Spider(scrapy.Spider):
    name = 'exhibition105'
    allowed_domains = ['jinshasitemuseum.com']
    start_urls = ['http://www.jinshasitemuseum.com/Exhibition/ExhibitionBasicDisplay']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=105
        li_list=response.xpath("/html/body/div[3]/div/div[2]/div[3]/div[2]/div[1]/div/div")
        for li in li_list:
            item["exhibitionIntroduction"] =''
            item["exhibitionTheme"]=li.xpath("./dl/dd/text()").extract_first()
            item["exhibition_picture"]=li.xpath("./dl/a/dt/img/@src").extract_first()
            yield item
        