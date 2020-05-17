# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
class Exhibition122Spider(scrapy.Spider):
    name = 'exhibition122'
    allowed_domains = ['dtxsmuseum.com']
    start_urls = ['http://www.dtxsmuseum.com/news_pic_list.aspx?category_id=24']
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=122
        li_list=response.xpath("/html//div/form/div[4]/div[2]/ul/li")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("./a/span/text()").extract_first()
            item["exhibitionIntroduction"]=''
            item["exhibition_picture"]='http://www.dtxsmuseum.com'+li.xpath("./a/span/img/@src").extract_first()
            yield item
        