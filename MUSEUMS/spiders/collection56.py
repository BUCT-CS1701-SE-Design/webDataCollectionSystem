# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import collection75Item


class Collection56Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection56'
    allowed_domains = ['hzmuseum.com']
    start_urls = ['http://www.hzmuseum.com/collection.aspx']

    def parse(self, response):
        li_list=response.xpath("//div[@class='txt']/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=56
            item["collectionImage"]='http://www.hzmuseum.com/'+li.xpath("./div[@class='div1']/a/img/@src").extract_first()
            item["collectionName"]=li.xpath("./div[@class='div2']/a/text()").extract_first()
            url='http://www.hzmuseum.com/'+li.xpath("./div[@class='div2']/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item},
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        
        p_list=response.xpath("//div[@class='txt']/p[@class='MsoNormal']")
        #print(p_list)
        content=''
        for p in p_list:
            sp=p.xpath('./span')
            for s in sp:
                if s.xpath("./text()").extract_first() is not None:

                    content+=s.xpath("./text()").extract_first()
                
        item["collectionIntroduction"]=content
        yield item   

        
