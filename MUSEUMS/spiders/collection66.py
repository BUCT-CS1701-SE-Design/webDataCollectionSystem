# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item



class Collection66Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection66'
    allowed_domains = ['rjjng.com.cn']
    start_urls = ['http://www.rjjng.com.cn/treasure/yjww.html']

    def parse(self, response):
        li_list=response.xpath("//div[@class='mainbar_pic_nr']/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=66
            item["collectionName"]=li.xpath("./a/@title").extract_first()
            item["collectionImage"]=li.xpath("./a/img/@src").extract_first()
            url=li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["collectionIntroduction"]=response.xpath("//div[@class='mainbar_content']/p[3]/text()").extract_first()
        yield item
