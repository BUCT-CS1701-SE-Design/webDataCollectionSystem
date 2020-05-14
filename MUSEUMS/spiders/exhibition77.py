# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }

class Exhibition77Spider(scrapy.Spider):
    name = 'exhibition77'
    allowed_domains = ['lymuseum.com']
    start_urls = ['http://www.lymuseum.com/list.php?fid=61']

    def parse(self, response):
        
        d_list=response.xpath("//tr/td/div")
        for d in d_list:
            item=exhibition75Item()
            item["museumID"]=77
            item["exhibitionTheme"]=d.xpath("./p/a/@title").extract_first()
            item["exhibition_picture"]=d.xpath("./p/a/img/@src").extract_first()
            url1=d.xpath("./p/a/@href").extract_first()
            if url1 is not None:
                url='http://www.lymuseum.com/'+url1
                #print(url)
                yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
            
    def parse_detail(self,response):
        item=response.meta["item"]
        content=response.xpath("//tr/td/p/span/text()").extract_first()
        #print(content)
        item["exhibitionIntroduction"]=content
        item["exhibitionTime"]=''
        yield item 
