# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition127Spider(scrapy.Spider):
    name = 'exhibition127'
    allowed_domains = ['nxbwg.com']
    start_urls = ['https://www.nxbwg.com/c/zlzs.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=127
        li_list=response.xpath("/html//div[1]/div[2]/div[2]/main/div/div/div/article")
        for li in li_list:
            item['exhibitionTime']=li.xpath("./div[1]/span/text()").extract_first()
            item["exhibitionTheme"]=li.xpath("./div[1]/h3/a/text()").extract_first()
            item['exhibitionIntroduction']=li.xpath("normalize-space(./div[2]/div[2]/text())").extract_first()
            item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\u2003', u'')
            item["exhibition_picture"]=str(li.xpath("./div[2]/div[1]/img/@src").extract_first())
            yield item
        