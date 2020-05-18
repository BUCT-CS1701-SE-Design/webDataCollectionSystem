# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from MUSEUMS.items import collection75Item

class Collection105Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection105'
    allowed_domains = ['jinshasitemuseum.com']
    start_urls = ['http://www.jinshasitemuseum.com/Treasure']

    def parse(self, response):
        li_list = response.xpath("/html//div[3]/div/div[2]/div/div/div[1]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 105
            item["collectionName"] = li.xpath("./p/text()").extract_first()
            item["collectionIntroduction"] = li.xpath("./div/img/@name2").extract_first()
            item["collectionImage"] =li.xpath("./div/img/@src").extract_first()
            yield item


        #yield item 

