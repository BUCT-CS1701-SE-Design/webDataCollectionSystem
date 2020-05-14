# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection6'
    allowed_domains = ['luxunmuseum.com.cn']
    start_urls = ['http://www.luxunmuseum.com.cn/cangshu/']
    
    def parse(self, response):
        li_list=response.xpath("//div[@class='content_shougao']/dl")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=6
            url='http://www.luxunmuseum.com.cn'+li.xpath("./dd/a/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item['collectionName']=response.xpath("//div[@class='main_content']/div[@class='content_title']/text()").extract_first()
        item['collectionImage']='http://www.luxunmuseum.com.cn'+response.xpath("//div[@class='main_content']/div[@class='content_nr']/div/img/@src").extract_first()
        divlist=response.xpath("//div[@class='main_content']/div[@class='content_nr']/div[2]/div")
        content=""
        for i in divlist :
          x=i.xpath("./text()").extract_first()
          if x!=None:
              content+=x
        item['collectionIntroduction']=content
        if content!="":
         yield item

        



