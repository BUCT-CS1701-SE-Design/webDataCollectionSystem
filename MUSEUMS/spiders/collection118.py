# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from MUSEUMS.items import collection75Item

class Collection118Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection118'
    allowed_domains = ['beilin-museum.com']
    start_urls = ['http://www.beilin-museum.com/channels/19.html']

    def parse(self, response):
        li_list = response.xpath("//table[4]//table[2]//td[3]/table[3]//tr[1]//ul")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 118
            item["collectionName"] = li.xpath("./li/a/text()").extract_first()
            url =li.xpath("./li/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["collectionIntroduction"] =' '
        item["collectionImage"] =response.xpath("//table[4]//table[2]//td[3]/table[3]//div[3]//@src").extract_first()

        yield item

