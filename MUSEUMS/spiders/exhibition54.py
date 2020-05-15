# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item

class Exhibition54Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition54'
    allowed_domains = ['chinasilkmuseum.com']
    start_urls = ['http://www.chinasilkmuseum.com/zz/list_17.aspx']

    def parse(self, response):
        li_list=response.xpath("/html/body/div[1]/div/div[2]/div/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=54
            item["exhibitionTheme"]=li.xpath("./div/h3/a/text()").extract_first()
            item["exhibition_picture"]='http://www.chinasilkmuseum.com/'+li.xpath("./a/img/@src").extract_first()
            item["exhibitionIntroduction"]=''
            item["exhibitionTime"]=li.xpath("./div/p[1]/text()").extract_first()
            yield item