# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item


class Collection68Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection68'
    allowed_domains = ['aymuseum.com']
    start_urls = ['http://www.aymuseum.com/nd.jsp?id=767#_jcp=4_2']

    def parse(self, response):
        item=collection75Item()
        item["museumID"]=68
        item["collectionName"]=response.xpath("//div[@class='newsDetail newsDetailV2']/h1/text()").extract_first()
        #item["collectionImage"]=response.xpath("//div[@class='richContent richContent0']/p/span/img/@src").extract_first()
        item["collectionImage"]='http://www.aymuseum.com'+response.xpath("//div[@class='newsDetail newsDetailV2']/div[2]/p/span/img/@src").extract_first()
        content=response.xpath("//div[@class='newsDetail newsDetailV2']/div[2]/p[7]/span/text()").extract_first()
        content+=response.xpath("//div[@class='newsDetail newsDetailV2']/div[2]/p[8]/span/text()").extract_first()
        item["collectionIntroduction"]=content
        yield item