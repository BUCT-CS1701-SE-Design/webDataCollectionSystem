# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
class Exhibition106Spider(scrapy.Spider):
    name = 'exhibition106'
    allowed_domains = ['zgshm.cn']
    start_urls = ['http://www.zgshm.cn/imglist.jsp?id=78abd44f3517405da73197aa6e9b0ccb']
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=106
        li_list=response.xpath("/html/body/ul/li")
        for li in li_list:
            item["exhibitionIntroduction"] =''
            item["exhibitionTheme"]=li.xpath("./div/label/text()").extract_first()
            item["exhibition_picture"]='http://www.zgshm.cn'+li.xpath("./img/@src").extract_first()
            yield item
        