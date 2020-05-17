# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item

class Exhibition62Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition62'
    allowed_domains = ['mtybwg.org.cn']
    start_urls = ['http://www.mtybwg.org.cn/zhanlan/105-1.aspx']

    def parse(self, response):
        l_list=response.xpath("/html/body/div[2]/div[2]/ul/li")
        for l in l_list:
            item=exhibition75Item()
            item["museumID"]=62
            item["exhibitionTheme"]=l.xpath("./a/img/@alt").extract_first()
            item["exhibition_picture"]='http://www.mtybwg.org.cn'+l.xpath("./a/img/@src").extract_first()
            url='http://www.mtybwg.org.cn'+l.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item},
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["exhibitionIntroduction"]=response.xpath("/html/body/div[2]/div[2]/ul/ul[2]/p[1]/text()").extract_first()
        if response.xpath("/html/body/div[2]/div[2]/ul/ul[2]/p[3]/span/text()").extract_first() is not None:
            item["exhibitionIntroduction"]+=response.xpath("/html/body/div[2]/div[2]/ul/ul[2]/p[3]/span/text()").extract_first()
        if response.xpath("/html/body/div[2]/div[2]/ul/ul[2]/p[5]/span/text()").extract_first() is not None:
            item["exhibitionIntroduction"]+=response.xpath("/html/body/div[2]/div[2]/ul/ul[2]/p[5]/span/text()").extract_first()
        item["exhibitionTime"]=''
        yield item
        