# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item

class Collection76Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection76'
    allowed_domains = ['hnzzmuseum.com']
    start_urls = ['http://www.hnzzmuseum.com/collection5_list.html']
    
    def parse(self, response):
        li_list=response.xpath("//div[@class='bd']/ul[@class='picList da-thumbs']/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=76
            item["collectionName"]=li.xpath("./a/div/p/span[@class='bd_con_t']/text()").extract_first()
            item["collectionIntroduction"]=li.xpath("./a/div/p/span[@class='bd_con_c']/text()").extract_first()
            item["collectionImage"]='http://www.hnzzmuseum.com'+li.xpath("./a/img/@src").extract_first()
            yield item