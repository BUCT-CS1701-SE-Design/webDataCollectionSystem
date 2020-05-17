# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item



class Exhibition68Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition68'
    allowed_domains = ['aymuseum.com']
    start_urls = ['http://www.aymuseum.com/nd.jsp?id=766#_jcp=4_2']

    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=68
        item["exhibitionTheme"]=response.xpath("//div[@class='newsDetail newsDetailV2']/h1/text()").extract_first()
        #item["collectionImage"]=response.xpath("//div[@class='richContent richContent0']/p/span/img/@src").extract_first()
        item["exhibition_picture"]='http://www.aymuseum.com'+response.xpath("//div[@class='newsDetail newsDetailV2']/div[2]/p/span/img/@src").extract_first()
        content=response.xpath("//div[@class='newsDetail newsDetailV2']/div[2]/p[7]/span/text()").extract_first()
        content+=response.xpath("//div[@class='newsDetail newsDetailV2']/div[2]/p[8]/span/text()").extract_first()
        item["exhibitionIntroduction"]=content
        item["exhibitionTime"]=''
        yield item
