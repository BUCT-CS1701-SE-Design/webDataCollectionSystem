# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from items import collection75Item

class Collection116Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection116'
    allowed_domains = ['yagmjng.com']
    start_urls = ['http://www.yagmjng.com/rsf/site/jinianguan/wenwujianshang/index.html']

    def parse(self, response):
        li_list = response.xpath("//div[2]/div[2]/div[2]/div/div[2]/div")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 116
            item["collectionName"] = li.xpath("./div[2]/a/text()").extract_first()
            item["collectionImage"] ="http://www.yagmjng.com/"+li.xpath("./div[1]/a/img/@src").extract_first()
            url ='http://www.yagmjng.com/'+li.xpath("./div[1]/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["collectionIntroduction"] =''

        yield item

