# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from items import collection75Item

class Collection127Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection127'
    allowed_domains = ['nxbwg.com']
    start_urls = ['https://www.nxbwg.com/c/jpww.html']

    def parse(self, response):
        li_list = response.xpath("//div[@class='item pb-item grid__item']")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 127
            item["collectionName"] = li.xpath("./h3/a/text()").extract_first()
            item["collectionImage"] =li.xpath(".//img/@src").extract_first()
            url ='https://www.nxbwg.com'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]

        p_list = response.xpath("//p[@style='text-align:justify;'] | //div[@style='text-align:justify;']/p")
        content = ""
        for p in p_list:
            x = p.xpath("./text()").extract_first()
            if x != None:
                content += x
                # break
        # print(content)
        item["collectionIntroduction"] = content
        yield item

