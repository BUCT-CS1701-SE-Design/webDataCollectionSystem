# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item



class Collection69Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection69'
    allowed_domains = ['qingdaomuseum.com']
    start_urls = ['http://www.qingdaomuseum.com/collection/category/16']

    def parse(self, response):
        d_list=response.xpath("/html/body/div[6]/div[2]/div/div[2]/div")
        for d in d_list:
            item=collection75Item()
            item["museumID"]=69
            item["collectionName"]=d.xpath("./div/h5/b/text()").extract_first()
            item["collectionImage"]=d.xpath("./div/div/a/img/@src").extract_first()
            url=d.xpath("./div/div/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        content=response.xpath("/html/body/div[6]/div[2]/div/div[4]/div/p/text()").extract_first()
        item["collectionIntroduction"]=content
        yield item