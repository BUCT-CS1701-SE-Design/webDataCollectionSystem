# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection47Spider(scrapy.Spider):
    name = 'collection47'
    allowed_domains = ['szmuseum.com']
    start_urls = ['http://www.szmuseum.com/Collection/List/ltgb']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        content_list = response.xpath("//div[@class='collectdetailbg']")
        li_list = response.xpath("//ul[@class='gcimglist clearfix']/li")
        count = 0
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 47
            item["collectionImage"] = li.xpath(".//img/@src").extract_first().strip()
            item["collectionName"] = li.xpath(".//p/text()").extract_first().strip()
            content = content_list[count].xpath(".//p/text()|.//span/text()").extract()
            content = "".join(content).strip()
            item["collectionIntroduction"] = content
            count += 1
            yield item


        
