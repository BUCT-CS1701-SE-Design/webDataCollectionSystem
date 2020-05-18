# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    name = 'exhibition75'
    allowed_domains = ['chnmus.net']
    start_urls = ['http://www.chnmus.net/template/viewList?page=1&catalogId=10c40ca2d1144146a241171338dc2f9b']
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=75
        li_list=response.xpath("//div[@class='colInfoBox']/ul/li")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("./h5/a/text()").extract_first()
            item["exhibition_picture"]='http://www.chnmus.net'+li.xpath("./a/img/@src").extract_first()
            yield item
        