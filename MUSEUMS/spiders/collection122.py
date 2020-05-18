# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from MUSEUMS.items import collection75Item

class Collection122Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection122'
    allowed_domains = ['dtxsmuseum.com']
    start_urls = ['http://www.dtxsmuseum.com/news_pic_list.aspx?category_id=29']

    def parse(self, response):
        li_list = response.xpath("//form/div[4]/div[2]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 122
            item["collectionName"] = li.xpath("./a/span[2]/text()").extract_first()
            item["collectionImage"] ="http://www.dtxsmuseum.com"+li.xpath("./a/span[1]/img/@src").extract_first()
            url ='http://www.dtxsmuseum.com/'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        p_list=response.xpath("//span")
        content=""
        for p in p_list:
            x=p.xpath("normalize-space(./text())").extract_first()
            if x != None:
                content+=x
                #break
        #print(content)
        item["collectionIntroduction"]=content.replace(u'|',u'')
        yield item
