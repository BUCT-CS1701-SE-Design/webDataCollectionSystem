# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition4'
    allowed_domains = ['jb.mil.cn']
    start_urls = ['http://www.jb.mil.cn/zlcl/jdcl/']
    
    def parse(self, response):
        li_list=response.xpath("//div[@class='ywzc_wrap']/div[@class='ywzc_leftWrap']/div[@class='ywzc_box']")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=4
            src=li.xpath("./a/img[@class='ywzcImg']/@src").extract_first()
            item["exhibition_picture"]='http://www.jb.mil.cn/zlcl/jdcl'+src[1:]
            item["exhibitionTheme"]=li.xpath("./h3[@class='ywzc_bt']/text()").extract_first()
            url=li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
             
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list = response.xpath("//p[@align='justify']")
        content=""
        for p in p_list:
            content+=p.xpath("./text()").extract_first()
        item["exhibitionIntroduction"]=content
        yield item

        



