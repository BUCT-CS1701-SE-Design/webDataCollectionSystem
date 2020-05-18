# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition115Spider(scrapy.Spider):
    name = 'exhibition115'
    allowed_domains = ['bmy.com.cn']
    start_urls = ['http://www.bmy.com.cn/html/public/zl/70c3ad1f3b3444cf84b1a8b8301fe093.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=115
        li_list=response.xpath("/html//div[3]/div[2]/div[2]/a")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("./div[2]/div[2]/p[2]/text()").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./div[2]/div[2]/p[1]/text()").extract_first()
            item["exhibition_picture"]=''
            yield item
        