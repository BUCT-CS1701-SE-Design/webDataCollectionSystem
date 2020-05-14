# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection7'
    allowed_domains = ['capitalmuseum.org.cn']
    start_urls = ['http://www.capitalmuseum.org.cn/jpdc/qb.htm']
    
    def parse(self, response):
        img_list=response.xpath("//td[@height='108']/a/img/@src").extract()
        name_list=response.xpath("//td[@height='21']/a/text()").extract()
        url_list=response.xpath("//td[@height='21']/a/@href").extract()
        for i in range(12):
            item=collection75Item()
            item["museumID"]=7
            item['collectionName']=name_list[i]
            item['collectionImage']='http://www.capitalmuseum.org.cn/jpdc/'+img_list[i]
            url='http://www.capitalmuseum.org.cn/jpdc/'+url_list[i]
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list=response.xpath("//div[@style='TEXT-ALIGN: left']/p/text()").extract()
        content=""
        for p in p_list:
            content+=p
        item['collectionIntroduction']=content
        yield item

        




