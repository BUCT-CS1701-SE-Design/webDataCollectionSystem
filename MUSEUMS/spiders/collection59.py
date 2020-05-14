# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

class Collection59Spider(scrapy.Spider):
    name = 'collection59'
    allowed_domains = ['museum.fjsen.com']
    start_urls = ['http://museum.fjsen.com/node_167182.htm']

    def parse(self, response):
        u_list=response.xpath("//div[@class='cont-bg']/div[@class='cont-left']/ul[@class='list_page']")
        for u in u_list:
            li_list=u.xpath("./li")
            for li in li_list:
                item=collection75Item()
                item["museumID"]=59
                item["collectionName"]=li.xpath("./a/text()").extract_first()
                url=li.xpath("./a/@href").extract_first()
                yield scrapy.Request(
                    url,
                    callback=self.parse_detail,
                    meta={"item":item}
                )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["collectionImage"]=response.xpath("//tr/td[@id='new_message_id']/p/img/@src").extract_first()
        #print(item)
        item["collectionIntroduction"]=response.xpath("//tr/td[@id='new_message_id']/p[2]/text()").extract_first()
        yield item