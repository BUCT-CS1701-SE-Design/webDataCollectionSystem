# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item



class Exhibition69Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition69'
    allowed_domains = ['qingdaomuseum.com']
    start_urls = ['http://www.qingdaomuseum.com/exhibition/category/16']

    def parse(self, response):
        d_list=response.xpath("/html/body/div[6]/div[2]/div[2]/div[1]/div")
        for d in d_list:
            item=exhibition75Item()
            item["museumID"]=69
            item["exhibitionTheme"]=d.xpath("./div/a/div/h4/text()").extract_first()
            item["exhibition_picture"]=d.xpath("./div/a/img/@src").extract_first()
            url=d.xpath("./div/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        content=response.xpath("/html/body/div[6]/div[2]/div/div[4]/p[1]/text()").extract_first()
        if response.xpath("/html/body/div[6]/div[2]/div/div[4]/p[2]/text()").extract_first() is not None:

            content+=response.xpath("/html/body/div[6]/div[2]/div/div[4]/p[2]/text()").extract_first()
        item["exhibitionIntroduction"]=content
        item["exhibitionTime"]=''
        yield item