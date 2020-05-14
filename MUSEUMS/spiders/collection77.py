# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

class Collection77Spider(scrapy.Spider):
    name = 'collection77'
    allowed_domains = ['lymuseum.com']
    start_urls = ['http://www.lymuseum.com/list.php?fid=46']

    def parse(self, response):
        d_list=response.xpath("//tr/td/div")
        for d in d_list:
            item=collection75Item()
            item["museumID"]=77
            item["collectionName"]=d.xpath("./p/a/@title").extract_first()
            item["collectionImage"]=d.xpath("./p/a/img/@src").extract_first()
            url1=d.xpath("./p/a/@href").extract_first()
            #print(url1)
            if url1 is not None:
                url='http://www.lymuseum.com/'+url1
                yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
            
    def parse_detail(self,response):
        item=response.meta["item"]
        
        item["collectionIntroduction"]=response.xpath("//tr/td/div/span/text()").extract_first()
        #print(item)
        yield item
