# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection3'
    allowed_domains = ['gmc.org.cn']
    start_urls = ['http://www.gmc.org.cn/mineral.html']
    
    def parse(self, response):
        li_list=response.xpath("//div[@class='clist clear']/div[@class='li']")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=3
            url='http://www.gmc.org.cn'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item['collectionName']=response.xpath("//div[@class='r']/div[@class='t28']/text()").extract_first()
        item['collectionImage']='gmc.org.cn'+response.xpath("//div[@class='limg']/img/@src").extract_first()
        p_list=response.xpath("//div[@class='r']/div[@class='con']/div[@class='p']/p")
        content=''
        for p in p_list:
            content+=p.xpath("./text()").extract_first()
        item['collectionIntroduction']=content
        yield item

        


