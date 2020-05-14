# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }

class Exhibition65Spider(scrapy.Spider):
    name = 'exhibition65'
    allowed_domains = ['jxmuseum.cn']
    start_urls = ['http://www.jxmuseum.cn/Exhibition/TempDisplayList/tzjl']

    def parse(self, response):
        li_list=response.xpath("//div[@id='divList']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=65
            item["exhibition_picture"]=li.xpath("./a/img/@src").extract_first()
            url ='http://www.jxmuseum.cn'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["exhibitionTheme"]=response.xpath("//div[@class='maindetail']/h1/text()").extract_first()
        p_list=response.xpath("//div[@class='maindetail']/div[@class='cont']/p")
        content=''
        for p in p_list:
            if p.xpath("./text()").extract_first() is not None:

                content+=p.xpath("./text()").extract_first()
        item["exhibitionIntroduction"]=content
        item["exhibitionTime"]=''
        yield item