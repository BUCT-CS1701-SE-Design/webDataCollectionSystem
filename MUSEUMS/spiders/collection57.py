# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import collection75Item

class Collection57Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

    name = 'collection57'
    allowed_domains = ['ahm.cn']
    start_urls = ['https://www.ahm.cn/Collection/Index/Collection']

    def parse(self, response):
        #print(response.text)
        li_list=response.xpath("//div[@class='col-sort']/ul/li")
        for li  in li_list:
            url='https://www.ahm.cn'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta=None,
            )
    def parse_detail(self,response):
        li_list=response.xpath("//div[@id='articles']/ul[@class='col-list']/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=57
            item["collectionImage"]=li.xpath("./a/div/img/@src").extract_first()
            item["collectionName"]=li.xpath("./a/div[@class='cont']/h3/text()").extract_first()
            url1='https://www.ahm.cn'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url1,
                callback=self.parse_detail2,
                meta={"item":item},
            )
    def parse_detail2(self,response):
        item=response.meta["item"]
        #content=response.xpath("//li[@class='share']/div[@calss='social-share share-component']/@data-title").extract_first()
        content=response.xpath("/html/body/div[3]/div/div[2]/div[1]/div[2]/ul/li[3]/div/@data-title").extract_first()
        item["collectionIntroduction"]=content
        yield item