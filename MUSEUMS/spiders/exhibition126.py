# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
class Exhibition126Spider(scrapy.Spider):
    name = 'exhibition126'
    allowed_domains = ['nxgybwg.com']
    start_urls = ['http://www.nxgybwg.com/e/action/ListInfo/?classid=12']
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=126
        li_list=response.xpath("/html//div[2]/div/div[2]/div[2]/div[2]/dl")
        for li in li_list:
            item['exhibitionTime']=li.xpath("./dt/span/text()").extract_first()
            item["exhibitionTheme"]=li.xpath("./dt/a/text()").extract_first()
            item['exhibitionIntroduction']=li.xpath("normalize-space(./dd[2]/text()[1])").extract_first()
            item["exhibitionIntroduction"] = str(item["exhibitionIntroduction"]).replace(u'\u3000', u'')
            item["exhibition_picture"]=str(li.xpath("./dd[1]/a/img/@src").extract_first())
            yield item
        