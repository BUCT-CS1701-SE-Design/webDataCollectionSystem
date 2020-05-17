# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
class Exhibition121Spider(scrapy.Spider):
    name = 'exhibition121'
    allowed_domains = ['bjqtm.com']
    start_urls = ['http://www.bjqtm.com/index.php?ac=article&at=list&tid=48']
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=121
        li_list=response.xpath("/html//div/div[1]/div[2]/div[3]/ul/li")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("./span/a/text()").extract_first()
            item["exhibition_picture"]='http://www.bjqtm.com/'+li.xpath("./a/img/@src").extract_first()
            yield item
        