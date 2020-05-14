# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }


class Collection62Spider(scrapy.Spider):
    name = 'collection62'
    allowed_domains = ['mtybwg.org.cn']
    start_urls = ['http://www.mtybwg.org.cn/cangpin.aspx']

    def parse(self, response):
        li_list=response.xpath("//div[@class='rightcon']/ul/li")
        for li in li_list:
            
            url=li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_deatil,
            )
    def parse_deatil(self,response):
        l_list=response.xpath("//div[@class='rightcon']/ul/li")
        for l in l_list:
            item=collection75Item()
            item["museumID"]=62
            item["collectionName"]=l.xpath("./a[@class='tag2']/text()").extract_first()
            item["collectionImage"]='http://www.mtybwg.org.cn'+l.xpath("./a/img/@src").extract_first()
            url1='http://www.mtybwg.org.cn'+l.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url1,
                callback=self.parse_deatil2,
                meta={"item":item}
            )
    def parse_deatil2(self,response):
        item=response.meta["item"]
        item["collectionIntroduction"]=response.xpath("//div[@class='pluscon']/ul/text()").extract_first()
        yield item
