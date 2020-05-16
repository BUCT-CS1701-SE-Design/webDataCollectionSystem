# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition52Spider(scrapy.Spider):
    name = 'exhibition52'
    allowed_domains = ['wzmuseum.cn']
    start_urls = ['http://www.wzmuseum.cn/Col/Col25/Index.aspx']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        li_list = response.xpath("//ul[@class='exbul']/li")
        for li in li_list:
            item = exhibition75Item()
            item["museumID"] = 52
            item["exhibition_picture"] = 'http://www.wzmuseum.cn' + li.xpath(".//img/@src").extract_first().strip()
            item["exhibitionTheme"] = li.xpath(".//div[@class='titlebox']/span/text()").extract_first().strip()
            content = li.xpath(".//div[@class='exbtxt']/p/text()|.//div[@class='exbtxt']/text()").extract()
            content = "".join(content).strip()
            item["exhibitionIntroduction"] = content
            yield item
        
