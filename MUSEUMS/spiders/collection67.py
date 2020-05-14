# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

class Collection67Spider(scrapy.Spider):
    name = 'collection67'
    allowed_domains = ['81-china.com']
    start_urls = ['http://www.81-china.com/collect/60.html']

    def parse(self, response):
        li_list=response.xpath("//div[@class='list_content']/ul/li")
        #print(li_list)
        for li in li_list:
            item=collection75Item()
            item["museumID"]=67
            item["collectionName"]=li.xpath("./div[1]/a/@title").extract_first()
            item["collectionImage"]='http://www.81-china.com'+li.xpath("./div[1]/a/img/@src").extract_first()
            item["collectionIntroduction"]=''
            yield item