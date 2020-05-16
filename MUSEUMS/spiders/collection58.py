# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import collection75Item


class Collection58Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection58'
    allowed_domains = ['hzwhbwg.com']
    start_urls = ['http://www.hzwhbwg.com/index.php/list-3-1.html']

    def parse(self, response):
        li_list=response.xpath("//div[@class='product']/ul/li")
        #print(li_list)
        for li in li_list:
            item=collection75Item()
            item["museumID"]=58
            item["collectionName"]='未知'
            item["collectionIntroduction"]=''
            item["collectionImage"]='http://www.hzwhbwg.com'+li.xpath("./a/img/@src").extract_first()
            yield item
        nexturl='http://www.hzwhbwg.com'+response.xpath("//div[@class='product']/p/a[5]/@href").extract_first()
        #print(nexturl)
        if nexturl is not None:

            yield scrapy.Request(
                nexturl,
                callback=self.parse,
            )
