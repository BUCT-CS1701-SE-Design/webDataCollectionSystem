# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition118Spider(scrapy.Spider):
    name = 'exhibition118'
    allowed_domains = ['beilin-museum.com']
    start_urls = ['http://www.beilin-museum.com/channels/13.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=118
        li_list=response.xpath("/html//table[4]//tr/td/table[2]//tr/td[3]/table[3]//tr[1]/td/div/ul/li")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("./a/text()").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./span/text()").extract_first()
            item["exhibition_picture"]=''
            yield item
        