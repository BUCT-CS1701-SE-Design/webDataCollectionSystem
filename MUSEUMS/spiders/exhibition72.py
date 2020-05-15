# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item



class Exhibition72Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition72'
    allowed_domains = ['sdmuseum.com']
    start_urls = ['http://www.sdmuseum.com/channels/ch00017/']

    def parse(self, response):
        d_list=response.xpath("/html/body/div[3]/div")
        for d in d_list:
            item=exhibition75Item()
            item["museumID"]=72
           
            item["exhibitionTheme"]=d.xpath("./div[@class='zl2-con']/div/a/text()").extract_first()
            item["exhibition_picture"]='http://www.sdmuseum.com'+d.xpath("./div[@class='zl2-pic']/a/img/@src").extract_first()
            item["exhibitionIntroduction"]=d.xpath("./div[@class='zl2-con']/div[2]/a/text()").extract_first()
            item["exhibitionTime"]=''
            yield item
