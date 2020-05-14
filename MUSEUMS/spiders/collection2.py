# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection2'
    allowed_domains = ['cstm.cdstm.cn']
    start_urls = ['http://cstm.cdstm.cn/e/action/ListInfo/?classid=209']
    
    def parse(self, response):
        li_list=response.xpath("//ul[@class='fen-zhanqu-zp-list']/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=2
            item["collectionName"]=li.xpath("./a[@class='fen-zhanqu-zp-name']/@title").extract_first()
            item["collectionImage"]='cstm.cdstm.cn'+li.xpath("./a[@class='fen-zhanqu-zp-pic']/img/@src").extract_first()
            url='http://cstm.cdstm.cn'+li.xpath("./a[@class='fen-zhanqu-zp-name']/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list=response.xpath("//div[@class='fen-info-cont']/p")
        content= ''
        for p in p_list:
            x= p.xpath("./text()").extract_first()
            if x!=None:
                content+=x
        item["collectionIntroduction"]=content
        yield item

        

