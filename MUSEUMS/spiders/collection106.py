# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from MUSEUMS.items import collection75Item

class Collection106Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection106'
    allowed_domains = ['zgshm.cn']
    start_urls = ['http://www.zgshm.cn/gczp.html']

    def parse(self, response):
        li_list = response.xpath("/html//div[4]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 106
            item["collectionName"] = li.xpath("./a/text()").extract_first()
            item["collectionImage"] ="http://www.zgshm.cn/"+li.xpath("./img/@src").extract_first()
            url ='http://www.zgshm.cn/'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["collectionIntroduction"] = response.xpath("normalize-space(//p/span)").extract_first()

        yield item


