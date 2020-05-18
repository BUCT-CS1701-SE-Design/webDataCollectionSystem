# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    name = 'exhibition16'
    allowed_domains = ['www.tjnhm.com']
    start_urls = ['https://www.tjnhm.com/index.php?p=zlxx_show&id=34&lanmu=2',
                  'https://www.tjnhm.com/index.php?p=zlxx_show&id=30&lanmu=2',
                  'https://www.tjnhm.com/index.php?p=zlxx_show&id=33&lanmu=2']
    def parse(self, response):
            item=exhibition75Item()
            item["museumID"]=16
            item["exhibitionTheme"]=response.xpath("//div[@id='aboutus_text']/h1/text()").extract_first()
            img_list=response.xpath("//img[@alt='']/@src").extract()
            item["exhibition_picture"]='www.tjnhm.com/'+img_list[0]
            list=response.xpath("//p[@style='text-align:left;']/span[@style='font-size:16px;font-family:NSimSun;']")
            content=""
            for p in list:
                content+=p.xpath("./text()").extract_first()
            item["exhibitionIntroduction"]=content
            yield item  

