# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }


class Exhibition67Spider(scrapy.Spider):
    name = 'exhibition67'
    allowed_domains = ['81-china.com']
    start_urls = ['http://www.81-china.com/zhanlan/57.html']

    def parse(self, response):
        li_list=response.xpath("//div[@class='list_content']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=67
            item["exhibitionTheme"]=li.xpath("./div[@class='left_listcon']/a/@title").extract_first()
            item["exhibition_picture"]='http://www.81-china.com'+li.xpath("./div[@class='left_listcon']/a/img/@src").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./div[@class='right_listcon']/p/text()").extract()
            item["exhibitionIntroduction"]=''.join(item["exhibitionIntroduction"])
            item["exhibitionTime"]=''
            yield item