# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from items import collection75Item

class Collection108Spider(scrapy.Spider):
    name = 'collection108'
    allowed_domains = ['ynmuseum.org']
    start_urls = ['http://www.ynmuseum.org/appreciate/gem/bronze.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    def parse(self, response):
        li_list = response.xpath("/html//div/div[3]/div[1]/div[2]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 108
            item["collectionName"] = li.xpath("./a/div[2]/text()").extract_first()
            item["collectionImage"] ="http://www.zgshm.cn/"+li.xpath("./a/div[1]/img/@src").extract_first()
            url ='http://www.ynmuseum.org'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["collectionIntroduction"] = response.xpath("normalize-space(//div[2]//div[2]/div[2]/div//div/text())").extract_first()

        yield item

