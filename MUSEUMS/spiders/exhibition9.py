# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition9'
    allowed_domains = ['www.1937china.com/kzjng']
    start_urls = ['http://www.1937china.com/kzjng/views/clzl/clzl_jbcl.html']
    def parse(self, response):
        li_list = response.xpath("//li[@class='carousel-cell']")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=9
            item["exhibitionTheme"]=li.xpath("./article/div[@class='col-content']/h3/a/text()").extract_first()
            item["exhibition_picture"]='http://www.1937china.com/kzjng/views'+li.xpath("./article/div[@class='col-image']/a/img/@src").extract_first()[2:]
            item["exhibitionIntroduction"]=li.xpath("./article/div[@class='col-content']/div[@class='f--desc']/p/text()").extract_first()
            yield item
       
       

        






