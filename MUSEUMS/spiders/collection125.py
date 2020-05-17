# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from items import collection75Item

class Collection125Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection125'
    allowed_domains = ['tour.dha.ac.cn']
    start_urls = ['http://tour.dha.ac.cn/list.aspx?id=715037769780']

    def parse(self, response):
        li_list = response.xpath("//tr")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 125
            item["collectionName"] = li.xpath("..//div[2]/div[1]/a/text()").extract_first()
            item["collectionIntroduction"] = li.xpath(".//div//div[2]/text()").extract_first()
            item["collectionImage"] ='(http://tour.dha.ac.cn)'+str(li.xpath(".//a/img/@src").extract_first())
            yield item

