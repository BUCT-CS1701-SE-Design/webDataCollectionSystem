# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }


class Exhibition61Spider(scrapy.Spider):
    name = 'exhibition61'
    allowed_domains = ['qzhjg.cn']
    start_urls = ['http://www.qzhjg.cn/html/gdzl/']

    def parse(self, response):
        li_list=response.xpath("//div[@class='exhibitionList']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=61
            item["exhibitionTheme"]=li.xpath("./div[@class='info']/h3/text()").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./div[@class='info']/p/text()").extract_first()
            item["exhibition_picture"]='http://www.qzhjg.cn'+li.xpath("./div[@class='thumb']/a/img/@src").extract_first()
            item["exhibitionTime"]=''
            yield item