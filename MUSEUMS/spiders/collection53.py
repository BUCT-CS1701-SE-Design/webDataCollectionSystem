# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

class Collection53Spider(scrapy.Spider):
    name = 'collection53'
    allowed_domains = ['zmnh.com']
    start_urls = ['http://www.zmnh.com/henryhtml/collection.html']

    def parse(self, response):
        d_list=response.xpath("//div[@class='contentt1']/div[3]")
        print(d_list)

        '''d_list=response.xpath("//div/div/div")
        print(d_list)
        for d in d_list:
            item=collection75Item()
            item["museumID"]=53
            print(item)
            item["collectionName"]=d.xpath("./div[@class='img_shade  com-flex-display com-flex-items-center']/span/text()").extract_first()
            item["collectionImage"]=d.xpath("./div[@class='item']/img/@src").extract_first()
            
            print(item)'''
           
