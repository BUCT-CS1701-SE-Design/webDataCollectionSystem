# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition114Spider(scrapy.Spider):
    name = 'exhibition114'
    allowed_domains = ['sxhm.com']
    start_urls = ['http://www.sxhm.com/index.php?ac=article&at=list&tid=194']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=114
        li_list=response.xpath("/html/body/div[3]/div[2]/div[2]/ul/li")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("./a/span/text()").extract_first()
            item["exhibitionIntroduction"]=' '
            item["exhibition_picture"]='http://www.sxhm.com/'+li.xpath("./a/img/@src").extract_first()
            yield item
        