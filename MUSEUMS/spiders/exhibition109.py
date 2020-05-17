# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
class Exhibition109Spider(scrapy.Spider):
    name = 'exhibition109'
    allowed_domains = ['ynnmuseum.com']
    start_urls = ['http://www.ynnmuseum.com/products_list.html']
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=109
        li_list=response.xpath("/html//div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/ul/li")
        for li in li_list:
            item["exhibitionTheme"] = li.xpath("normalize-space(./div[2]/ul/li/h1/strong/a/text())").extract_first()
            item["exhibitionTheme"] = str(item["exhibitionTheme"]).replace(u'\\xa0', u' ')
            item["exhibitionTheme"] = str(item["exhibitionTheme"]).replace(u'\xa0', u' ')
            if len(item["exhibitionTheme"]) != 0:
                item["exhibitionIntroduction"] = li.xpath("normalize-space(./div[2]/div/text())").extract_first()
                item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\\xa0', u' ')
                item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\xa0', u' ')
                item["exhibition_picture"] = 'http://www.ynnmuseum.com' + str(li.xpath("./div[1]/div/a/img/@src").extract_first())





