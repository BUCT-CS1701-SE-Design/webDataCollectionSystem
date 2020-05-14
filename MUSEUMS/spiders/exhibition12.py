# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition12'
    allowed_domains = ['www.ciae.com.cn']
    start_urls = ['http://www.ciae.com.cn/display/zh/civilization.html']
    def parse(self, response):
        li_list=response.xpath("//div[@class='body_box bg_com']/div[@class='basic']/div[@class='wrap']/div[@id='ajax-list']/ul[@class='basic_list cf']/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=12
            item["exhibitionTheme"]=li.xpath("./a/div[@class='tit']/h3/text()").extract_first()
            item["exhibition_picture"]='http://www.ciae.com.cn'+li.xpath("./a/div[@class='tran_scale']/img/@src").extract_first()
            url='http://www.ciae.com.cn'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list=response.xpath("//div[@class='content']/p/text()").extract()
        old=response.xpath("//div[@class='content']/p[@align='center']/text()").extract()
        content=""
        for p in p_list:
            if p not in old:
                content+=p
        item["exhibitionIntroduction"]=content
        yield item
       
       

        









