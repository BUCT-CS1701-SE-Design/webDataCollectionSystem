# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item

class Collection54Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection54'
    allowed_domains = ['chinasilkmuseum.com']
    start_urls = ['http://www.chinasilkmuseum.com/zggd/list_21.aspx']

    def parse(self, response):
        li_list=response.xpath("/html/body/div[1]/div/div[5]/div/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=54
            item["collectionName"]=li.xpath("./p/a/text()").extract_first()
            item["collectionImage"]='http://www.chinasilkmuseum.com'+li.xpath("./a/img/@src").extract_first()
            url='http://www.chinasilkmuseum.com'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item},
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list=response.xpath("/html/body/div[1]/div/div[2]/div/div[2]/p")
        content=''
        #for p in p_list:
            #content+=p.xpath("./text()").extract_first
        item["collectionIntroduction"]=content
        yield item 
            
