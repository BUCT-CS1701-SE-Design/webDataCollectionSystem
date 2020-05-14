# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }


class Exhibition66Spider(scrapy.Spider):
    name = 'exhibition66'
    allowed_domains = ['rjjng.com.cn']
    start_urls = ['http://www.rjjng.com.cn/display/topics.html']

    def parse(self, response):
        li_list=response.xpath("//div[@class='mainbar_pic_nr']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=66
            item["exhibitionTheme"]=li.xpath("./a/@title").extract_first()
            item["exhibition_picture"]=li.xpath("./a/img/@src").extract_first()
            item["exhibitionTime"]=''
            item["exhibitionIntroduction"]=''
            yield item
