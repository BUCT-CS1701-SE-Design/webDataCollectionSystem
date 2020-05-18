# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition10'
    allowed_domains = ['www.zkd.cn']
    start_urls = ['http://www.zkd.cn/jbcl/index.jhtml']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    def parse(self, response):
        li_list = response.xpath("//div[@class='xszz_list']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=10
            item["exhibitionTheme"]=li.xpath("./div[@class='nr_list']/div[@class='ming2']/text()").extract_first()
            item["exhibition_picture"]='www.zkd.cn'+li.xpath("./img/@src").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./div[@class='nr_list']/div[@class='jieshao2']/text()").extract_first()
            yield item
       
       

        







