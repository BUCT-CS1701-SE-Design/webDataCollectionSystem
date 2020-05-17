# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from items import collection75Item

class Collection117Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection117'
    allowed_domains = ['hylae.com']
    start_urls = ['http://www.hylae.com/index.php?ac=article&at=list&tid=37']

    def parse(self, response):
        li_list = response.xpath("/html//div[3]/div[2]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 117
            item["collectionName"] = li.xpath("./span[2]/a/text()").extract_first()
            item["collectionImage"] ="http://www.hylae.com/"+li.xpath("./span[1]/a/img/@src").extract_first()
            url =li.xpath("./span/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]

        p_list = response.xpath("//div[3]/div[2]/div[3]/p")
        content = ""
        for p in p_list:
            x = p.xpath("./text()").extract_first()
            if x != None:
                content += x
                # break
        # print(content)
        item["collectionIntroduction"] = content
        yield item

