# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition15'
    allowed_domains = ['www.tjbwg.com']
    start_urls = ['https://www.tjbwg.com/cn/exhibitionInfo.aspx?Id=16968',
                  'https://www.tjbwg.com/cn/exhibitionInfo.aspx?Id=16972',
                  'https://www.tjbwg.com/cn/exhibitionInfo.aspx?Id=16971',
                  'https://www.tjbwg.com/cn/exhibitionInfo.aspx?Id=16970']
    def parse(self, response):
            item=exhibition75Item()
            item["museumID"]=15
            item["exhibitionTheme"]=response.xpath("//div[@class='mainC maxW1100']/div[@class='exhibition exhibitionD']/div[@class='tit_menu_ex']/h3/text()").extract_first()
            item["exhibition_picture"]='www.tjbwg.com'+response.xpath("//div[@class='mainC maxW1100']/div[@class='exhibition exhibitionD']/div[@class='exh_us clearfix']/div[@class='exhUs_l']/div[@class='img']/img/@src").extract_first()
            item["exhibitionIntroduction"]=response.xpath("//div[@class='mainC maxW1100']/div[@class='exhibition exhibitionD']/div[@class='exh_us clearfix']/div[@class='exhUs_r']/p/text()").extract_first()
            yield item  
