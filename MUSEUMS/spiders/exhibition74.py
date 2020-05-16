# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item

class Exhibition74Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }

    name = 'exhibition74'
    allowed_domains = ['wfsbwg.com']
    start_urls = ['http://www.wfsbwg.com/list/?50_1.html']

    def parse(self, response):
        li_list=response.xpath("//div[@class='list_contentt']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=74
            item["exhibitionTheme"]=li.xpath("./div/a/@title").extract_first()
            item["exhibition_picture"]='http://www.wfsbwg.com'+li.xpath("./div/a/img/@src").extract_first()
            url='http://www.wfsbwg.com'+li.xpath("./div/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["exhibitionTime"]=''
        content=response.xpath("/html/body/div[7]/div[2]/div[2]/div[2]/div[1]/div/p[3]/span/text()").extract()
        item["exhibitionIntroduction"]=''.join(content)
        yield item
