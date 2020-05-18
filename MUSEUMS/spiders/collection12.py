# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline

class Collection75Spider(scrapy.Spider):
    name = 'collection12'
    allowed_domains = ['www.ciae.com.cn']
    start_urls = ['http://www.ciae.com.cn/collection/zh/collection.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    def parse(self, response):
        li_list=response.xpath("//div[@class='vip_down1 boutique3']/div[@class='wrap']/div[@class='content']/div[@class='list']/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=12
            item['collectionName']=li.xpath("./a/@title").extract_first()
            item['collectionImage']='http://www.ciae.com.cn/'+li.xpath("./a/div[@class='img tran_scale']/img/@src").extract_first()
            url='http://www.ciae.com.cn/'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item['collectionIntroduction']=response.xpath("//div[@class='content']/div[@class='text']/div[@class='p']/text()").extract_first()
        yield item

        








