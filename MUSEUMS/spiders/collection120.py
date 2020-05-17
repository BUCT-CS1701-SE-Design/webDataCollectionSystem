# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from items import collection75Item

class Collection120Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection120'
    allowed_domains = ['xabwy.com']
    start_urls = ['http://www.xabwy.com/SitePage.aspx?ID=132']

    def parse(self, response):

        d_list = response.xpath("//div[@class='infolist01']")
        for d in d_list:
            dy = d.xpath(".//li")
            for dd in dy:
                item = collection75Item()
                item["museumID"] = 120
                item["collectionImage"] = dd.xpath(".//img/@src").extract_first()
                item["collectionName"] = dd.xpath(".//a/text()").extract_first()
                url =dd.xpath(".//a/@href").extract_first()

                    #处理详 情页
                yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item": item}  # 传递参数
                    )

    def parse_detail(self, response):
        item = response.meta["item"]
        p_list=response.xpath("//p")
        content=""
        for p in p_list:
            x=p.xpath("normalize-space(.//text())").extract_first()
            if x != None:
                content+=x
                #break
        #print(content)
        item["collectionIntroduction"]=content
        yield item

