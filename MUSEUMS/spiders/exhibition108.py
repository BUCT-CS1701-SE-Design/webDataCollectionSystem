# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition108Spider(scrapy.Spider):
    name = 'exhibition108'
    allowed_domains = ['ynmuseum.org']
    start_urls = ['http://www.ynmuseum.org/exhibition/display.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=108
        li_list=response.xpath("/html//div/div[3]/div[1]/div/div[3]/div[1]/div")
        for li in li_list:
            item["exhibitionTheme"] = li.xpath("normalize-space(./div[2]/div/div[1])").extract_first()
            #item["exhibitionTheme"] = str(item["exhibitionTheme"]).replace(u'\\xa0', u' ')
            #item["exhibitionTheme"] = str(item["exhibitionTheme"]).replace(u'\xa0', u' ')
            item["exhibitionIntroduction"] ='' #li.xpath(
            #   "normalize-space(./div/div/div/div/div[1]/div[2]/div/text())").extract_first()
            #item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\\xa0', u' ')
            # item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\xa0', u' ')
            item["exhibition_picture"] = 'http://www.ynmuseum.org'+li.xpath('./div[1]/a/img/@src').extract_first()

            yield item
        