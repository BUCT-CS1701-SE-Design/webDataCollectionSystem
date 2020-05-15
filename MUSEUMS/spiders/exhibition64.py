# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item


class Exhibition64Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition64'
    allowed_domains = ['jgsgmbwg.com']
    start_urls = ['http://www.jgsgmbwg.com/bwgnews.php?cid=7']

    def parse(self, response):
        li_list=response.xpath("//div[@class='subCont']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=64
            item["exhibitionTheme"]=li.xpath("./span[@class='title']/a/text()").extract_first()

            url='http://www.jgsgmbwg.com/'+li.xpath("./span[@class='title']/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item},
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        
        item["exhibitionIntroduction"]=response.xpath("//div[@id='textarea']/text()").extract_first()
        item["exhibitionTime"]=''
        item["exhibition_picture"]=''
        yield item