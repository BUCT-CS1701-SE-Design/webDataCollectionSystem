# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item


class Collection72Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection72'
    allowed_domains = ['sdmuseum.com']
    start_urls = ['http://www.sdmuseum.com/channels/ch00079/']

    def parse(self, response):
        #t=response.xpath("/html/body/div[3]/div[2]/table/tr/td/table/tr[4]/td/table/tr")
        #print(t)
        tr_list=response.xpath("/html/body/div[3]/div[2]/table/tr/td/table/tr[4]/td/table/tr")
        #print(response.text)
        for td_list in tr_list:
            td=td_list.xpath("./td")
            for t in td:
                item=collection75Item()
                item["museumID"]=72
                item["collectionImage"]='http://www.sdmuseum.com'+t.xpath("./div/div/a/img/@src").extract_first()
                item["collectionName"]=t.xpath("./div/div[2]/a/text()").extract_first()
                url='http://www.sdmuseum.com'+t.xpath("./div/div/a/@href").extract_first()
                #print(url)
                yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["collectionIntroduction"]=response.xpath("/html/body/div[3]/div[2]/div[2]/div/p[3]/span[2]/text()").extract_first()
        
        yield item




