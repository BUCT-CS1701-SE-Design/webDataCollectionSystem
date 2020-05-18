# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import collection75Item

class Collection61Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

    name = 'collection61'
    allowed_domains = ['qzhjg.cn']
    start_urls = ['http://www.qzhjg.cn/dcwc/index.jhtml']

    def parse(self, response):
        li_list=response.xpath("//div[@class='thumbList']/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=61
            item["collectionName"]=li.xpath("./a/p/text()").extract_first()
            item["collectionImage"]='http://www.qzhjg.cn'+li.xpath("./a/img/@src").extract_first()

            url='http://www.qzhjg.cn'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                    url,
                    callback=self.parse_detail,
                    meta={"item":item}
                )
    def parse_detail(self,response):
        item=response.meta["item"]
        #item["collectionIntroduction"]=response.xpath("//div[@class='picshowtxt']/div[@class='picshowtxt_right']/text()").extract_first()
        item["collectionIntroduction"]=response.xpath("//div[@class='picmidmid']/ul/li[1]/a/img/@text").extract_first()
        yield item
