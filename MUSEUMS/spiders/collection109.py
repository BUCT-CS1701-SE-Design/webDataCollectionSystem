# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from MUSEUMS.items import collection75Item

class Collection109Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection109'
    allowed_domains = ['ynnmuseum.com']
    start_urls = ['http://www.ynnmuseum.com/products_list1.html']

    def parse(self, response):
        li_list=response.xpath("/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 109
            if li.xpath(".//div[1]/div/a/img/@src").extract_first() is not None:

                item["collectionName"] =li.xpath("./div[2]/ul/li/h1/strong/a/@title").extract_first()
            
                item["collectionImage"] ='http://www.ynnmuseum.com'+li.xpath("./div[1]/div/a/img/@src").extract_first()
                url='http://www.ynnmuseum.com'+li.xpath("./div[1]/div/a/@href").extract_first()
                yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["collectionIntroduction"] = response.xpath("/html/body/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/form[1]/div[2]/div/div/p[1]/text()").extract_first()
        yield item 
         

        