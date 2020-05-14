# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }


class Exhibition59Spider(scrapy.Spider):
    name = 'exhibition59'
    allowed_domains = ['museum.fjsen.com']
    start_urls = ['http://museum.fjsen.com/node_167181.htm']

    def parse(self, response):
        u_list=response.xpath("//div[@class='cont-bg']/div[@class='cont-left']/ul[@class='list_page']")
        #print(u_list)
        for u in u_list:
            li_list=u.xpath("./li")
            for li in li_list:
                item=exhibition75Item()
                item["museumID"]=59
                item["exhibitionTheme"]=li.xpath("./a/text()").extract_first()
                url=li.xpath("./a/@href").extract_first()
                yield scrapy.Request(
                    url,
                    callback=self.parse_detail,
                    meta={"item":item}
                )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["exhibition_picture"]=response.xpath("//tr/td[@id='new_message_id']/p/img/@src").extract_first()
        item["exhibitionIntroduction"]=response.xpath("//tr/td[@id='new_message_id']/p[3]/text()").extract_first()
        item["exhibitionTime"]=''
        yield item
        #item["exhibitionIntroduction"]=re