# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition125Spider(scrapy.Spider):
    name = 'exhibition125'
    allowed_domains = ['tour.dha.ac.cn']
    start_urls = ['http://tour.dha.ac.cn/list.aspx?id=715037769780']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=125
        li_list=response.xpath("//tr")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath(".//div[2]/div[1]/a/text()").extract_first()
            item["exhibitionIntroduction"]=li.xpath(".//div//div[2]/text()").extract_first()
            item["exhibition_picture"]='(http://tour.dha.ac.cn)'+str(li.xpath(".//a/img/@src").extract_first())
            yield item
        