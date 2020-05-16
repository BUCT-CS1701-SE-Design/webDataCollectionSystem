# -*- coding: utf-8 -*-
import scrapy
import re 
from MUSEUMS.items import collection75Item


class Collection73Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection73'
    allowed_domains = ['ytmuseum.com']
    start_urls = ['http://www.ytmuseum.com/diancang.html']

    def parse(self, response):
        li_list=response.xpath("//div[@class='conf']/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=73
            if li.xpath("./a/img/@src").extract_first() is not None:

                item["collectionImage"]='http://www.ytmuseum.com'+li.xpath("./a/img/@src").extract_first()
                item["collectionName"]=li.xpath("./div/a/text()").extract_first()
                url='http://www.ytmuseum.com'+li.xpath("./a/@href").extract_first()
                yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["collectionIntroduction"]=response.xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td/text()").extract_first()
        if response.xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td/text()[1]").extract_first() is not None:

            item["collectionIntroduction"]=response.xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td/text()").extract_first()
        elif item["collectionIntroduction"] is None:
            item["collectionIntroduction"]=response.xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/text()").extract_first()
        elif item["collectionIntroduction"] is None:
            item["collectionIntroduction"]=response.xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/p[3]/text()[1]").extract_first()
        elif item["collectionIntroduction"] is None:
            item["collectionIntroduction"]=response.xpath("/html/body/div[3]/div[3]/div[2]/div[2]/div[3]/p[2]/text()").extract_first()
        else:
            pass
        if item["collectionIntroduction"] is not None:

            item["collectionIntroduction"]= ''.join(item["collectionIntroduction"].split())
        yield item
