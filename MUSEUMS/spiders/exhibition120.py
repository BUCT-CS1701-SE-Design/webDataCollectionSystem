# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition120Spider(scrapy.Spider):
    name = 'exhibition120'
    allowed_domains = ['xabwy.com']
    start_urls = ['http://www.xabwy.com/SitePage.aspx?ID=208']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=120
        li_list=response.xpath("/html//div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("./div/div[1]/div[1]/div/a/text()").extract_first()
            item["exhibitionIntroduction"]=''
            item["exhibition_picture"]=li.xpath("./div/div[2]/a/img/@src").extract_first()
            yield item
        