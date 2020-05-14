# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition13'
    allowed_domains = ['www.bjp.org.cn']
    start_urls = ['http://www.bjp.org.cn/art/2014/1/10/art_195_1670.html','http://www.bjp.org.cn/art/2014/1/10/art_195_1669.html','http://www.bjp.org.cn/art/2014/1/10/art_195_1668.html','http://www.bjp.org.cn/art/2014/1/11/art_195_1741.html']
    def parse(self, response):
            item=exhibition75Item()
            item["museumID"]=13
            item["exhibitionTheme"]=response.xpath("//meta[@name='title']/@content").extract_first()
            item["exhibition_picture"]='www.bjp.org.cn'+response.xpath("//p[@style='text-align:center;']/img/@src").extract_first()
            item["exhibitionIntroduction"]=response.xpath("//p/text()").extract_first()
            yield item     
       

        










