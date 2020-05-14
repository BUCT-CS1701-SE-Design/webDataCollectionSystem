# -*- coding: utf-8 -*-
import scrapy
import re 
from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

class Collection74Spider(scrapy.Spider):
    name = 'collection74'
    allowed_domains = ['wfsbwg.com']
    start_urls = ['http://www.wfsbwg.com/list/?5_1.html']

    def parse(self, response):
        li_list=response.xpath("//div[@class='list_contentt']/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=74
            item["collectionImage"]='http://www.wfsbwg.com'+li.xpath("./div/a/img/@src").extract_first()
            item["collectionName"]=li.xpath("./div/a/@title").extract_first()
            item["collectionIntroduction"]=''
            yield item
        url=li.xpath("/html/body/div[7]/div[2]/div[3]/div/a[10]/@href").extract_first()
        nexturl='http://www.wfsbwg.com/list/'+url
        if nexturl is not None:
            yield scrapy.Request(
                nexturl,
                callback=self.parse
            )

