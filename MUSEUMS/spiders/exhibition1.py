# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition1'
    allowed_domains = ['dpm.org.cn']
    start_urls = ['https://www.dpm.org.cn/shows.html']
    
    def parse(self, response):
        li_list=response.xpath("//div[@id='temporary5']/div[@class='item']")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=1
            item["exhibitionTheme"]=li.xpath("./a[@target='_blank']/@title").extract_first()
            item["exhibition_picture"]=li.xpath("./a/img[@class='lazyload']/@data-src").extract_first()
            url='https://www.dpm.org.cn'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        
        p_list=response.xpath("//div[@class='content_edit']/@style").extract_first()
        item["exhibitionIntroduction"]=p_list
        yield item

        
