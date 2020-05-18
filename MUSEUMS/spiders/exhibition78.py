# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import exhibition75Item #声明使用的是那个Item

class Exhibition78Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition78'
    allowed_domains = ['nyhhg.com']
    start_urls = ['http://www.nyhhg.com/a/jx/']

    def parse(self, response):
        
        li_list=response.xpath("//div[@class='content']/ul[@class='newslist']/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=78
            item["exhibitionTheme"]=li.xpath("./div/a/@title").extract_first()
            item["exhibition_picture"]='http://www.nyhhg.com'+li.xpath("./div/a/img/@src").extract_first()
            url='http://www.nyhhg.com'+li.xpath("./div[@class='txt']/p/a/@href").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./div[@class='txt']/p/text()").extract_first()
            #print(item)
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item},
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list=response.xpath("//div[@class='content']/p")
        content=''
        for p in p_list:
            py=p.xpath("./span")
            for sp in py:
                content+=sp.xpath("./text()").extract_first()
        print(content)
        if content != '':
            item["exhibitionIntroduction"]=content
        item["exhibitionTime"]=''
        yield item