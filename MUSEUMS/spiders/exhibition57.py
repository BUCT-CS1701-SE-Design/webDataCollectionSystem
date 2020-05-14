# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }

class Exhibition57Spider(scrapy.Spider):
    name = 'exhibition57'
    allowed_domains = ['ahm.cn']
    start_urls = ['https://www.ahm.cn/Exhibition/TListNow/xztj']

    def parse(self, response):
        li_list=response.xpath("//ul[@class='exhibition-new']/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=57
            item["exhibitionTheme"]='见图'
            item["exhibition_picture"]=li.xpath("./a/div/img/@src").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./div/p[@class='detail']/text()").extract_first()
            item["exhibitionTime"]=li.xpath("./div/p[1]/text()").extract_first()
            yield item
