# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from items import collection75Item

class Collection126Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection126'
    allowed_domains = ['nxgybwg.com']
    start_urls = ['http://www.nxgybwg.com/e/action/ListInfo/?classid=17']

    def parse(self, response):
        li_list = response.xpath("//div[2]/div/div[2]/div[2]/div[2]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 126
            item["collectionName"] = li.xpath("./p/a/text()").extract_first()
            item["collectionImage"] =li.xpath(".//a/img/@src").extract_first()
            url ='http://www.nxgybwg.com'+li.xpath("./div/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]

        p_list = response.xpath("//p[@style='text-align: justify;']")
        content = ""
        for p in p_list:
            x = p.xpath("./text()").extract_first()
            if x != None:
                content += x
                # break
        # print(content)
        item["collectionIntroduction"] = content
        yield item

