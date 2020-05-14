# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

class Collection78Spider(scrapy.Spider):
    name = 'collection78'
    allowed_domains = ['nyhhg.com']
    start_urls = ['http://www.nyhhg.com/a/xy/']

    def parse(self, response):
        d_list=response.xpath("//div[@class='cateslist']/dl/dd")
        for d in d_list:
            item=collection75Item()
            item["museumID"]=78
            item["collectionName"]=d.xpath("./div/a/@title").extract_first()
            item["collectionImage"]='http://www.nyhhg.com'+d.xpath("./div/a/img/@src").extract_first()
            url='http://www.nyhhg.com'+d.xpath("./div/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item},
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["collectionIntroduction"]=response.xpath("//div/span/span/text()").extract_first()
        if item["collectionIntroduction"] is None:
            item["collectionIntroduction"]='请去官网查看'
        yield item