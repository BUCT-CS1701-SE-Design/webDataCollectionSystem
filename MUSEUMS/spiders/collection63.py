# -*- coding: utf-8 -*-
import scrapy
import re 
from MUSEUMS.items import collection75Item


class Collection63Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

    name = 'collection63'
    allowed_domains = ['www.crt.com.cn/mx/']
    start_urls = ['http://www.crt.com.cn/mx/gcww.html']

    def parse(self, response):
        print(response.text)
        li_list=response.xpath("//div[@id='picBox']/ul/li")
        print(li_list)
