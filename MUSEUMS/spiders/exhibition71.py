# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }


class Exhibition71Spider(scrapy.Spider):
    name = 'exhibition71'
    allowed_domains = ['bowuguan.qingzhou.gov.cn']
    start_urls = ['http://bowuguan.qingzhou.gov.cn/zl/']

    def parse(self, response):
        td_list=response.xpath("/html/body/div[2]/table/tbody/tr[3]/td/table")
        for td in td_list:
            item=exhibition75Item()
            item["museumID"]=71
            c=td.xpath("./tbody/tr[1]/td[2]/a/span/text()").extract_first()
            item["exhibitionTheme"]=''.join(c.split())
            item["exhibition_picture"]='http://bowuguan.qingzhou.gov.cn/zl/'+td.xpath("./tbody/tr[1]/td[1]/a/img/@src").extract_first()
            content=td.xpath("./tbody/tr[2]/td/text()").extract_first()
            #re.sub('\s', ' ', content)
            item["exhibitionIntroduction"]= ''.join(content.split())
            #item["exhibitionIntroduction"]=content
            item["exhibitionTime"]=''
            yield item

