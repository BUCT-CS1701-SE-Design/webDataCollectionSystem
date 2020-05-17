# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from items import collection75Item

class Collection114Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection114'
    allowed_domains = ['sxhm.com']
    start_urls = ['http://www.sxhm.com/index.php?ac=article&at=list&tid=218']

    def parse(self, response):
        li_list = response.xpath("//div[3]/div[2]/div[2]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 114
            item["collectionName"] = li.xpath("./a/span/text()").extract_first()
            item["collectionImage"] ="http://www.sxhm.com/"+li.xpath("./a/img/@src").extract_first()
            url =li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        p_list = response.xpath("//p/span")
        content = ""
        for p in p_list:
            x = p.xpath("./text()").extract_first()
            if x != None:
                content += x
                # break
        # print(content)
        item["collectionIntroduction"] = content
        yield item



