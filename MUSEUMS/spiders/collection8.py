# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection8'
    allowed_domains = ['www.bmnh.org.cn']
    start_urls = ['http://www.bmnh.org.cn/gzxx/gzbb/5/list.shtml']
    
    def parse(self, response):
        list=response.xpath("//div[@class='col-sm-4']")
        for i in list:
            item=collection75Item()
            item["museumID"]=8
            item['collectionName']=i.xpath("./div[@class='thumbnail']/a/img/@alt").extract_first()
            item['collectionImage']='www.bmnh.org.cn'+i.xpath("./div[@class='thumbnail']/a/img/@src").extract_first()
            item['collectionIntroduction']="暂无介绍"
            yield item


        





