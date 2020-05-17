# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 1,}
    }
class Exhibition116Spider(scrapy.Spider):
    name = 'exhibition116'
    allowed_domains = ['yagmjng.com']
    start_urls = ['http://www.yagmjng.com/rsf/site/jinianguan/jibenchenlie/index.html']
    
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=116
        li_list=response.xpath("/html//div[2]/div[2]/div[2]/div/div[2]/ul/li")
        for li in li_list:
            item["exhibitionTheme"]=li.xpath("./a/font/text()").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./span/text()").extract_first()
            item["exhibition_picture"]='http://www.yagmjng.com/'+li.xpath("./a/@href").extract_first()
            yield item
        