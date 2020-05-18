# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition45Spider(scrapy.Spider):
    name = 'exhibition45'
    allowed_domains = ['19371213.com.cn']
    start_urls = ['http://www.19371213.com.cn/exhibition/']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        li_list = response.xpath("//div[@class='view-content']/div[position()<last()]")
        for li in li_list:
            item = exhibition75Item()
            item["museumID"] = 45    
            image_url = li.xpath(".//img/@src").extract_first().strip()
            item["exhibition_picture"] = 'http://www.19371213.com.cn/exhibition' + image_url[1:]
            item["exhibitionTheme"] = li.xpath(".//h2/text()").extract_first().strip()
            content = li.xpath(".//p/text()|.//span/text()").extract()
            content = "".join(content).strip()
            item["exhibitionIntroduction"] = content
            yield item
        
