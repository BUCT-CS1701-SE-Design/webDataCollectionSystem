# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition3'
    allowed_domains = ['gmc.org.cn']
    start_urls = ['http://www.gmc.org.cn/permanent_exhibition.html']
    
    def parse(self, response):
        li_list=response.xpath("//div[@class='li']/div[@class='limg imgh']")
        li_list1=response.xpath("//div[@class='l imgh']")
        li_list2=response.xpath("//div[@class='r imgh']")
        li_list+=li_list1
        li_list+=li_list2
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=3
            item["exhibition_picture"]='http://www.gmc.org.cn'+li.xpath("./a/img/@src").extract_first()
            url='http://www.gmc.org.cn'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["exhibitionTheme"]=response.xpath("//div[@class='con']/div[@class='t28']/text()").extract_first()
        item["exhibitionIntroduction"]=response.xpath("//div[@class='pbox']/div[@class='p']/text()").extract_first()
        yield item

        


