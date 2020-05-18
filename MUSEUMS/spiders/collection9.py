# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline

class Collection75Spider(scrapy.Spider):
    name = 'collection9'
    allowed_domains = ['www.1937china.com/kzjng']
    start_urls = ['http://www.bmnh.org.cn/gzxx/gzbb/5/list.shtml']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    def parse(self, response):
        list=response.xpath("//div[@class='dc_list']/div[@class='dc_item']")
        for i in list:
            item=collection75Item()
            item["museumID"]=9
            item['collectionName']=i.xpath("./div[@class='dc_right_con']/div[@class='dc_title']/text()]").extract_first()
            item['collectionImage']='http://www.1937china.com/kzjng/views'
            item['collectionIntroduction']="暂无介绍"
            yield item


        






