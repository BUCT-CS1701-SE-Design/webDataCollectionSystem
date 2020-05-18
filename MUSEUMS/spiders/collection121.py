# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from MUSEUMS.items import collection75Item

class Collection121Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection121'
    allowed_domains = ['bjqtm.com']
    start_urls = ['http://www.bjqtm.com/index.php?ac=article&at=list&tid=52']

    def parse(self, response):
        li_list = response.xpath("//div[1]/div[2]/div[3]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 121
            item["collectionName"] = li.xpath("./span/a/text()").extract_first()
            item["collectionImage"] ="http://www.bjqtm.com/"+li.xpath("./a/img/@src").extract_first()
            url = li.xpath("./a/@href").extract_first()
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

