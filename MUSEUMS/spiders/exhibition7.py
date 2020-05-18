# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition7'
    allowed_domains = ['capitalmuseum.org.cn']
    start_urls = ['http://www.capitalmuseum.org.cn/zlxx/ztyscl.htm']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    def parse(self, response):
        Name_list=response.xpath("//td[@height='22']/text()").extract()
        Img_list=response.xpath("//td[@width='200']/img/@src").extract()
        Intro1_list=response.xpath("//td[@height='52']/text()").extract()
 
        for i in range(5):
            item=exhibition75Item()
            item["museumID"]=7
            item["exhibitionTheme"]=Name_list[i]
            item["exhibition_picture"]='http://www.capitalmuseum.org.cn/zlxx/'+Img_list[i]
            item["exhibitionIntroduction"]=Intro1_list[i*2]+Intro1_list[i*2+1]
            yield item

        




