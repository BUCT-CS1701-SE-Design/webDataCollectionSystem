# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item


class Exhibition56Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition56'
    allowed_domains = ['hzmuseum.com']
    start_urls = ['http://www.hzmuseum.com/exhibition.aspx']

    def parse(self, response):
        li_list=response.xpath("//div[@class='ul_exh']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=56
            item["exhibitionTheme"]=li.xpath("./div[@class='div2 rg']/p/a/text()").extract_first()
            item["exhibition_picture"]='http://www.hzmuseum.com/'+li.xpath("./div[@class='div1 lf']/a/img/@src").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./div[@class='div2 rg']/p[@class='p1']/text()").extract_first()
            item["exhibitionTime"]=li.xpath("./div[@class='div2 rg']/p[3]/text()").extract_first()
            yield item
