# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }


class Collection65Spider(scrapy.Spider):
    name = 'collection65'
    allowed_domains = ['jxmuseum.cn']
    start_urls = ['http://www.jxmuseum.cn/Collection/List/jpxs?subno=jpxs']

    def parse(self, response):
        li_list=response.xpath("//div[@id='divList']/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=65
            item["collectionName"]=li.xpath("./a/p/text()").extract_first()
            item["collectionImage"]=li.xpath("./a/i/img/@src").extract_first()
            url='http://www.jxmuseum.cn'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        #p_list=response.xpath("//div[@class='cont']/p").extract_first()
        item["collectionIntroduction"]=response.xpath("//div[@class='cont']/p[5]/text()").extract_first()
        yield item

