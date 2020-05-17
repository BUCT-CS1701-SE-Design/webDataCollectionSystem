# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
class Exhibition107Spider(scrapy.Spider):
    name = 'exhibition107'
    allowed_domains = ['zunyihy.cn']
    start_urls = ['http://www.zunyihy.cn/five_story.html']
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=107
        li_list=response.xpath("/html//div[4]/div/div/div")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("normalize-space(./a/span/text())").extract_first()
            item["exhibitionTheme"] = str(item["exhibitionTheme"]).replace(u'\\xa0', u' ')
            item["exhibitionTheme"] = str(item["exhibitionTheme"]).replace(u'\xa0', u' ')
            item["exhibitionIntroduction"]=li.xpath("normalize-space(./div/div/div/div/div[1]/div[2]/div/text())").extract_first()
            item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\\xa0', u' ')
            item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\xa0', u' ')
            item["exhibition_picture"] =''

            yield item
        