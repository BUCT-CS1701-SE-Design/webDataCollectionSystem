# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition112Spider(scrapy.Spider):
    name = 'exhibition112'
    allowed_domains = ['cmnh.org.cn']
    start_urls = ['https://www.cmnh.org.cn/list/?11.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=112
        li_list=response.xpath("/html//div[2]/div[3]/div[1]/ul/li")
        for li in li_list:
            item["exhibitionTheme"]='常设展厅'
            item["exhibitionIntroduction"]=li.xpath("normalize-space(./div/div/p[1]/text())").extract_first()
            item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\\xa0', u' ')
            item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\xa0', u' ')
            item["exhibition_picture"]='https://www.cmnh.org.cn'+li.xpath("./div/p/a/img/@src").extract_first()
            yield item
        